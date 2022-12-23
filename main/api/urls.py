from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('sentiment_text/',views.sentiment_text,name='sentiment_text'),
]