from django.contrib import admin
from django.urls import path

from .views import rekap

urlpatterns = [
    path('', rekap, name='rekap' )
]

