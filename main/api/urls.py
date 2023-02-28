from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import viewsSentiText, viewsSentiStat, viewsSentiImage, viewsSentiSpeech, viewsSentiOnline,viewsSentiTrans,viewsSentiFiles,views,viewsUrl
#import template view
from django.views.generic import TemplateView

urlpatterns = [
      path('history/', views.history, name='history'),
      path('senti_trans', viewsSentiTrans.senti_transalte, name='senti_trans'),
    path('sentiment_text/',viewsSentiText.sentiment_text,name='sentiment_text'),
    path('senti_stat/', viewsSentiStat.senti_stat, name='senti_stat'),
    path('upload_senti_stat/',viewsSentiStat.upload_senti_stat,name='upload_senti_stat'),
    path('senti_image', viewsSentiImage.senti_image, name='senti_image'),
    path('image_upload', viewsSentiImage.image_upload, name='image_upload'),
    path('senti_audio', viewsSentiSpeech.senti_audio, name='senti_audio'),
    path('audio_upload', viewsSentiSpeech.audio_upload, name='audio_upload'),
    path('senti_online', viewsSentiOnline.senti_online, name='senti_online'),
    path('detect_language', viewsSentiTrans.detect_language, name='detect_language'),
    path('senti_files',viewsSentiFiles.senti_files,name='senti_files'),
    path('files_upload',viewsSentiFiles.files_upload,name='files_upload'),
    path('loading',TemplateView.as_view(template_name='pages/loading.html'),name='output'),
    path('output',views.output,name='output'),
    path('senti_url',viewsUrl.senti_url,name='senti_url'),
    path('csv_download',views.csv_download,name='csv_download'),
    path('senti_url_submit',viewsUrl.senti_url_submit,name='senti_url_submit'),
    path('translate',viewsSentiTrans.translate,name='translate')
  

    # path('example/',views.example,name="example")
]