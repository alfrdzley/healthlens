from django.contrib import admin
from django.urls import path,include

from .views import rekap

urlpatterns = [
    path('rekap/', rekap, name='rekap' )
]

