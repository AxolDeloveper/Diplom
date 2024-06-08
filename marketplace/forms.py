from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput

from django import forms
from .models import Item


class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': PasswordInput
        }

        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        ]

        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Почта'
        }

class ForgottenPassword(forms.Form):
    email = forms.CharField(max_length=60)
    code = forms.CharField()
    new_password = forms.CharField()



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'image_one', 'image_two', 'image_three']

