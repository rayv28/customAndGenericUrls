from django.contrib import admin
from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
  path('fun1/',fun1,name='fun1'),
]