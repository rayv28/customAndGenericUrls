from django.contrib import admin
from django.urls import path
from app3.views import *
app_name='something2'
urlpatterns=[
  path('fun3/', fun3, name='fun3'),
]