from django.shortcuts import render
import requests
# import HTMLParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#Detected_language = "en"
from .emorec import senti_api
from collections import defaultdict
from googletrans import Translator
from deep_translator import GoogleTranslator
from .models import Response
#import redirct
from django.shortcuts import redirect
# Create your views here.
def senti_transalte(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userId=request.user.id
            text = request.POST.get('text-input')
            print(text)

          
            final_text = GoogleTranslator(source='auto', target='en').translate(text)
       

            print(final_text)
                        

            per = {'love':0,'joy':0,'anger':0,'sadness':0,'surprise':0,'fear':0}

            ans1 = [senti_api(final_text[:len(final_text)//4])]
            ans2 = [senti_api(final_text[len(final_text)//8: len(final_text)//4])]
            ans3 = [senti_api(final_text[len(final_text)//12:len(final_text)//8])]
            ans4 = [senti_api(final_text[len(final_text)//16:len(final_text)//12])]
            fin = []
            fin =  ans1 + ans2 + ans3 + ans4 




                # ans1 = [senti_api(final_text[:len(final_text)//6])]
                # ans2 = [senti_api(final_text[len(final_text)//6: len(final_text)//9])]
                # ans3 = [senti_api(final_text[len(final_text)//9:len(final_text)//12])]
                # ans4 = [senti_api(final_text[len(final_text)//12:len(final_text)//15])]
                # ans5 = [senti_api(final_text[len(final_text)//15:len(final_text)//18])]
                # ans6 = [senti_api(final_text[len(final_text)//18:])]
                # fin = []
                # fin =  ans1 + ans2 + ans3 + ans4 + ans5 + ans6

            sol = defaultdict(lambda : 0)
            for i in fin:
                if i in sol:
                    sol[i]+=1
                else:
                    sol[i] = 1



            #print({'fear':2,'sad':3,'happy':10})
            #print(sol)
            
            print('came till 102')
            for i,j in sol.items():
                per[i] = round(j/len(fin)*100,2)

            pos=0
            neg=0
            for i,j in per.items():
                if (i == 'love' or i == 'joy' or i == 'surprise') and j>0:
                    pos+=j
                elif (i == 'sadness' or i == 'fear' or i == 'anger')  and j>0:
                    neg+=j
            per['positive'] = pos
            per['negative'] = neg
            print(per)
            print(per)
            response={'data':per}

            json_response=json.dumps(response)
        


            servicePaths = {'input':text}
            print(servicePaths)
            responseData = json.dumps({'text':final_text})
            print(servicePaths)
            print("83")
            print(responseData)
            print("84")
            response_id=Response.objects.create(userid=request.user.id, service='Senti Files',servicepaths=servicePaths,serviceLocation=json_response,responsedata=responseData).id
            print(response_id)
            print(Response.objects.get(id=response_id).serviceLocation)
            responseId=response_id
            print(responseId)



            
            
            url='http://127.0.0.1:8000/output?responseId='+str(responseId)
            return redirect(url)
        else:
            return render(request,'pages/sentiTrans.html')
    else:
        return redirect('login')
import json
from langdetect import detect
from django.http import JsonResponse
from langdetect import detect
from django.views.decorators.csrf import csrf_exempt


# function to detect language
def detect_language(request):
    if request.method == 'POST':
        text = request.POST.get('text-input', '')
        api_key = 'YOUR_API_KEY'  # replace with your API key

        url = 'https://api.meaningcloud.com/lang-2.0'
        payload = {
            'key': api_key,
            'txt': text
        }
        response = requests.post(url, data=payload)

        if response.ok:
            language = response.json()['language_list'][0]['name']
            return JsonResponse({'result': f'The language of the text is {language}.'})
        else:
            return JsonResponse({'error': 'Unable to detect language.'})

# function to translate text to English
def translate(request):
    if request.method == 'POST':
        text = request.POST.get('text-input', '')
        api_key = 'YOUR_API_KEY'  # replace with your API key

        # detect the language of the input text
        url = 'https://api.meaningcloud.com/lang-2.0'
        payload = {
            'key': api_key,
            'txt': text
        }
        response = requests.post(url, data=payload)

        if response.ok:
            language = response.json()['language_list'][0]['name']

            # translate the text to English
            url = 'https://api.meaningcloud.com/translate-2.0'
            payload = {
                'key': api_key,
                'txt': text,
                'lang': f'{language}|en'
            }
            response = requests.post(url, data=payload)

            if response.ok:
                translation = response.json()['translated_text']
                return JsonResponse({'result': translation})
            else:
                return JsonResponse({'error': 'Unable to translate text.'})
        else:
            return JsonResponse({'error': 'Unable to detect language.'})