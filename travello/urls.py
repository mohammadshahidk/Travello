from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('news',views.news,name='news'),
    path('destinations',views.destinations,name='destinations'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
   
   
]
