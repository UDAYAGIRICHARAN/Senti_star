from django.shortcuts import render
import requests
# import HTMLParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def sentiment_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
     
      
        return render(request,'dashboard/sentiment_text.html',{'result':text})
    else:

        return render(request,'dashboard/sentiment_text.html')