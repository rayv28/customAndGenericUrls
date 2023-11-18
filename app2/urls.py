from django.contrib import admin
from django.urls import path
from app2.views import *
app_name='something1'
urlpatterns=[
  path('fun2/',fun2,name='fun2'),
]