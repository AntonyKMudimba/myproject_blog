from django.urls import path

from posts import views

urlpatterns = [
    #path('',HomeView.as_view(), name='home'),
    path('', views.Home, name='Home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),



]