from django.shortcuts import render
from .forms import FileUploadForm
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Files,Response
from django.http import JsonResponse
from PyPDF2 import PdfReader
import textract
#from pptx import Presentation
from .emorec import senti_api 
from collections import defaultdict
import csv
import json

def senti_files(request):

    if request.user.is_authenticated:
        print(request.POST)
        if request.method == 'POST':
            form=forms.FileUploadForm(request.POST, request.FILES)
            
            if form.is_valid():
                files = form.cleaned_data['files']
                userid = request.user.id
                path_list = []
                for file1 in files:
                    Image.objects.create(file=file1, user_id=userid)
                    path = file1.url
                    path_list.append(path)
                return render(request, 'pages/sentiFiles.html', {'path_list': path_list})
            else:
                return render(request, 'pages/sentiFiles.html', {'form': form})
        else:
            form = FileUploadForm()
            return render(request, 'pages/sentiFiles.html', {'form': form})
    else:
        return redirect('login')
def files_upload(request):
    print(request.POST)
    if request.method == 'POST' and request.user.is_authenticated:
            
            path_list = []
            for i in request.FILES.getlist('files'):
                path = ""
                filetype = i.content_type
                Files.objects.create(files=i, userid=request.user.id, filetype=filetype)
                #populate path_list with the paths to the images
                path = Files.objects.last().files.url
                path_list.append(path)


            print(path_list)
            sol = "E:/Major-Project/Major-Project SPEECH/main"
            per = {'love':0,'joy':0,'anger':0,'sadness':0,'surprise':0,'fear':0}
            ans = ''
            final_text=''
            for i in path_list:
                # PDF PARSIING
                if str(i).endswith('pdf'):
                    # creating a pdf reader object
                    reader = PdfReader(sol+i)
                    # getting a specific page from the pdf file
                    # extracting text from page
                    for k in range(len(reader.pages)):
                        page = reader.pages[k] 
                        text = page.extract_text()
                        final_text+=text
                elif str(i).endswith('doc') or str(i).endswith('docx'):
                    print(sol+i)
                    text = textract.process(sol+i)
                    final_text+=str(text)
                elif str(i).endswith('pptx'):
                    
                    prs = Presentation(sol+i)
                    for slide in prs.slides:
                        for shape in slide.shapes:
                            if hasattr(shape, 'text'):
                                ans+=shape.text
                    final_text+=ans
                elif str(i).endswith('csv'):
                    # opening the CSV file
                    with open(sol+i, mode ='r') as file:
                    
                    # reading the CSV file
                        csvFile = csv.reader(file)
                        lst = []
                    # displaying the contents of the CSV file
                        for lines in csvFile:
                                lst+=lines

                    str1 = " " 
                    final_text += str1.join(lst)

                elif str(i).endswith('txt'):
                    file1 = open(sol+i,"r+") 
                    final_text+=str(file1.read())


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
            responseData = json.dumps({'text':final_text})
            print(servicePaths)
            response_id=Response.objects.create(userid=request.user.id, service='Senti Files',servicepaths=servicePaths,serviceLocation=json_response,responsedata=responseData).id
            print(response_id)
            print(Response.objects.get(id=response_id).serviceLocation)
            responseId=response_id
        


            
            

            return JsonResponse({'responseId':responseId, 'status': 'success', 'message': 'File uploaded successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'File upload failed'})



