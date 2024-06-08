from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

import hashlib

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from marketplace.controllers.domain_controller import Domain
from marketplace.controllers.email_controller import EmailControlles
from marketplace.forms import UserForm, ForgottenPassword
from marketplace.models import Code, Item, Profile


# Create your views here.
def home(req):
    return render(req, 'base/base.html', {})
def register(request):
    error = None
    if request.method == 'POST':
        password = request.POST.get('password')

        try:
            new_user = User(
                username=request.POST.get('username'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email=request.POST.get('email')
            )

            new_user.set_password(request.POST.get('password'))

            new_user.save()
        except Exception as ex:
            error = ex


        return HttpResponseRedirect('/login')

    form = UserForm()

    form['username'].help_text = None


    return render(request, 'registration/reg.html', {
        'additional_title': 'Регистрация Пользователя',
        'form': form,
        'error': error
    })

def article(req, query):
    post = Item.objects.get(pk=query)
    return render(req, 'article.html', {
        'additional_title': 'Статья',
        'post': post
    })

def profile(req, query):
    user = User.objects.get(pk=query)
    return render(req, 'profile.html', {
        'additional_title': 'Профиль пользователя',
        'user': user
    })

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def forgotten_password(req):
    form = ForgottenPassword()
    if req.method == "POST":
        email = req.POST.get('email')

        users = User.objects.values_list('email', flat=True).distinct()

        if email not in users:
            return HttpResponse('404')
        email_controller = EmailControlles(str(email), "Код для сброса пароля:", 'Код ')
        email_controller.send_code()
        print(email_controller.codessss)
        domains = Domain()

        codes = Code(
            domain = domains,
            code = email_controller.code
        )
        codes.save()

        return HttpResponseRedirect(f'{domains}?email={email}&code={email_controller.code}')


    return render(req, 'registration/forgotten_password/step_1.html', {'form': ForgottenPassword})

def forgotten_password_2(req, slug):
    domains = Code.objects.values_list('domain', flat=True).distinct()

    if slug not in domains:
        return HttpResponseRedirect('/')

    email = req.GET.get('email')
    code = req.GET.get('code')

    if req.method == 'POST':
        form_code = req.POST.get('code')

        if form_code is not None:

            hashed_form_code = hashlib.sha256(form_code.encode()).hexdigest()

            if hashed_form_code == code:
                # getted_slug = req.path.split('/')[2]
                #
                # new_code = Code(
                #     domain=getted_slug,
                #     code=code
                # )
                # new_code.save()

                return HttpResponseRedirect(f'/user/{slug}?email={email}&old-{slug}')

    return render(req,'registration/forgotten_password/step_2.html', {'form': ForgottenPassword})

def forgotten_password_3(req, slug):
    domains = Code.objects.values_list('domain', flat=True).distinct()

    if slug not in domains:
        return HttpResponseRedirect('/')

    new_password = req.POST.get('new_password')
    email = req.GET.get('email')
    old_slug = req.GET.get('old')

    user = User.objects.get(email=email)


    user.set_password(new_password)
    user.save()


    codes = Code.objects.get(domain=slug)
    codes.delete()

    return render(req, 'registration/forgotten_password/step_3.html', {'form': ForgottenPassword})


def search(req, query):
    found_item = Item.objects.filter(title=query)

    return render(req, 'test.html', {
        'posts': found_item
    })

def items(req):
    item = Item.objects.all()
    return render(req, 'items.html', {
        'items': item
    })

@login_required
@transaction.atomic
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = request.user
            item.save()
            return redirect('items')
    else:
        form = ItemForm()

    return render(request, 'item_create.html', {'form': form})