from django.urls import path

from news import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('post/id/<int:query>', views.article, name='article'),
]