from django.urls import path
from django.contrib import admin
from accounts.views import login_page, register_page

urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
]