from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home import views
from . import views

urlpatterns = [ 
   path('', views.home, name='home'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name="contact"),
   path('services', views.services, name="contact"),
   path('faq', views.faq, name="contact"),
   path('team', views.team, name="contact"),
   path('signup', views.handleSignup, name='handleSignup'),
   path('login', views.handleLogin, name='handleLogin'),
   path('logout/', views.handleLogout, name='handleLogout'),
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name='home/password_reset.html'), name='password_reset'),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'), name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'), name='password_reset_confirm'),
   path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'), name='password_reset_complete'),
]