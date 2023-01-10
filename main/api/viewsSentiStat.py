from django.shortcuts import render
from django.http import HttpResponse


def senti_stat(request):
  #return hello world
    introduction= "Hello World"  
    return  render(request, 'pages/senti_stat.html', {'introduction':introduction})
def upload_senti_stat(request):
#    if method.request=="POST":
#        #read the file 
#         file_data= request.FILES['file']
#          #print the 
    return redirct('login')