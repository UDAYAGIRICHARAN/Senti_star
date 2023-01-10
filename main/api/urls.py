from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views, viewsSentiStat

urlpatterns = [
    path('sentiment_text/',views.sentiment_text,name='sentiment_text'),
    path('senti_stat/', viewsSentiStat.senti_stat, name='senti_stat'),
    path('upload_senti_stat/',viewsSentiStat.upload_senti_stat,name='upload_senti_stat'),
]