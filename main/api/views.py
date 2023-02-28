from django.shortcuts import render
from django.http import JsonResponse
from .forms import AudioUploadForm
from .models import Audio,Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
##import json
import json
##import Httpresponse
from django.shortcuts import render, HttpResponse
def output(request):
    print("in output")
    print(request.method)
    if request.method=='GET':
        responseId=request.GET.get('responseId')
    
   
        print(responseId)
        print(type(responseId))
        output={}
        
        for i in Response.objects.filter(id=responseId):
            output['response']=i.responsedata
            output['service']=i.service
            output['servicepaths']=i.servicepaths
            output['serviceLocation']={}
            print(i.serviceLocation)
            json_data = json.loads(i.serviceLocation)
            print(json_data)
            x_value=[]
            y_value=[]

            ## make i.serviceLocation values as string
            for key,value in json_data.items():
                output['serviceLocation'][key]={}
                for k,v in value.items():
                    output['serviceLocation'][key][k]=str(int(v))
                    if k!="positive" and k!="negative":
                        
                        x_value.append(int(v))
                        y_value.append(k)
            print(x_value)
            print(y_value)
            output['x_value']=x_value
            output['y_value']=y_value
        output['responseId']=responseId
          
            
    
      
      
      
        return render(request,'pages/output.html',{'output':output})
    else:
        print(request.method)
        print("in else")
        return 

        # return render(request,'pages/loading.html'def csv_download(request):
def csv_download(request):
    if request.method=='GET':
        responseId=request.GET.get('responseId')
    
   
        print(responseId)
        print(type(responseId))
        output={}
        
        for i in Response.objects.filter(id=responseId):
               output={}
               json_data=json.loads(i.serviceLocation)
               for key,value in json_data.items():
                    output[key]={}
                    for k,v in value.items():
                          output[key][k]=str(int(v))
                            
        print(output)
        output=dict(output)
        print(type(output['data']))


        import csv
  
        field_names = ["love", "joy", "anger", "sadness", "surprise", "fear", "positive", "negative"]
        
        cars = [output['data']]
        print(cars)
        ##erase the data from files/report.csv

        
        with open('files/report.csv', 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(cars)

        ##return csv file
        return HttpResponse(csvfile, content_type='text/csv',headers={'Content-Disposition': 'attachment; filename="report.csv"'})

def history(request):
    if request.method=='GET' and request.user.is_authenticated:
        output={}
        output['history']=[]
        for i in Response.objects.filter(userid=request.user.id):
            output['history'].append({'id':i.userid,'service':i.service,'servicepaths':i.servicepaths,'serviceLocation':i.serviceLocation,'responsedata':i.responsedata})
       
        return render(request,'pages/history.html',{'output':output})
    else:
        return render(request,'pages/history.html')