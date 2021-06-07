from django.contrib import admin
from django.urls import path
from .views import hello, home

urlpatterns = [
    path('hello/', hello, name="index"),
    path('', home),
]
