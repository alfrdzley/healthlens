from django.contrib import admin
from django.urls import path,include

from .views import rekap, upload
from . import views

urlpatterns = [
    path('rekap/', views.rekap, name='rekap' )
    path('upload/', views.upload, name='upload'),
]

