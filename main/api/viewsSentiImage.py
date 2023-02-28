from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .forms import ImageUploadForm
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Response
import json
from .emorec import senti_api 
import cv2
import easyocr
import warnings
from collections import defaultdict
warnings.filterwarnings("ignore")
        # from pylab import rcParams
        # rcParams['figure.figsize'] = 8, 16

def senti_image(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
        
            form = ImageUploadForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
            
           
                images = form.cleaned_data['images']
                userid = request.user.id

                path_list = []

                for image in images:
                    Image.objects.create(image=image, user_id=userid)
                    path = image.url

                    path_list.append(path)
                return render(request, 'senti-image/sentiImage.html', {'path_list': path_list})
            else:
                return render(request, 'senti-image/sentiImage.html', {'form': form})
                


                        
        else:
            form = ImageUploadForm()
            return render(request, 'senti-image/sentiImage.html', {'form': form})
    else:
        return redirect('login')
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm


def image_upload(request):


    if request.method == 'POST' and request.user.is_authenticated:
            path_list = []
            for i in request.FILES.getlist('images'):
                path = ""
                Image.objects.create(image=i, userid=request.user.id)
                #populate path_list with the paths to the images
                path = Image.objects.last().image.url
                path_list.append(path)
                
            
            print(path_list)
            #response sentiment analysis and ocr result
            final_text = ""
            reader = easyocr.Reader(['en'])
            sol = "E:/Major-Project/Major-Project SPEECH/main"
            per = {'love':0,'joy':0,'anger':0,'sadness':0,'surprise':0,'fear':0}
            text_dict = {}
            for i in range(len(path_list)):
                each_path=sol+path_list[i]
                print(each_path)
                output = reader.readtext(each_path)
                final_text = ""

                for _, text, __ in output: # _ = bounding box, text = text and __ = confident level
                    final_text += " "
                    final_text += text
                text_dict[str(i)] = final_text
              
                #print(final_text)

            # Call the sentiment api
            #ans = senti_api(final_text)

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

            response={'data':per}
            json_response=json.dumps(response)
            path_list = json.dumps(path_list)

            servicePaths = json.dumps({'path':path_list})
            responseData = json.dumps(text_dict)
            print(servicePaths)
            response_id=Response.objects.create(userid=request.user.id, service='Senti Image ',servicepaths=servicePaths,serviceLocation=json_response,responsedata=responseData).id
            print(response_id)
            print(Response.objects.get(id=response_id).serviceLocation)
            responseId=response_id
        


            
            

            return JsonResponse({'responseId':responseId, 'status': 'success', 'message': 'File uploaded successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'File upload failed'})
