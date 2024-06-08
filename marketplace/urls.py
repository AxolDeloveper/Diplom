from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
import os

urlpatterns = [
    path('', views.home, name='home_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/registration', views.register, name='registration'),
    path('item/id/<int:query>', views.article, name='article'),
    path('accounts/profile/<int:query>', views.profile, name='prof'),
    path('accounts/forgotten_password', views.forgotten_password, name='step-1'),
    path('accounts/<str:slug>/', views.forgotten_password_2, name='step-2'),
    path('user/<str:slug>/', views.forgotten_password_3, name='step-3'),
    path('search/<str:query>/', views.search, name='search'),
    path('account/registration', views.register, name='register'),
    path('create', views.create_item, name='create_item'),
    path('items', views.items, name='items')
]
if os.environ.get('RUN_MAIN') == 'true':
    from . import scheduler