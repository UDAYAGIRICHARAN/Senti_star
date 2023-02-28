from django.shortcuts import render
from django.http import JsonResponse
from .forms import AudioUploadForm
from .models import Audio,Response
import speech_recognition as sr
from .emorec import senti_api
import wavio
from collections import defaultdict
import soundfile
import json

def senti_audio(request):
    if request.user.is_authenticated:
        print(request.POST)
        if request.method == 'POST':
            form = AudioUploadForm(request.POST, request.FILES)
            #print(form)

            if form.is_valid():
                audios = form.cleaned_data['audio']
                userid = request.user.id
                path_list = []
                for audio in audios:
                    Audio.objects.create(audio=audio, user_id=userid)
                    path = audio.url
                    path_list.append(path)
                return render(request, 'pages/sentiSpeech.html', {'path_list': path_list})
            else:
                return render(request, 'pages/sentiSpeech.html', {'form': form})
        else:
            form = AudioUploadForm()
            return render(request, 'pages/sentiSpeech.html', {'form': form})
    else:
        return redirect('login')


def audio_upload(request):
    try:


        if request.method == 'POST' and request.user.is_authenticated:
                path_list = []
                print(request.POST)
                print(request.FILES)
                for i in request.FILES.getlist('audios'):    
                    path = ""
                    Audio.objects.create(audio=i, userid=request.user.id)
                    #populate path_list with the paths to the images
                    path = Audio.objects.last().audio.url
                    path_list.append(path)

                sol = "E:/Major-Project/Major-Project SPEECH/main"
                per = {'love':0,'joy':0,'anger':0,'sadness':0,'surprise':0,'fear':0}
                    #print(path_list)
                print("HERE IS : ",path_list)
                res = {}
                final_text = ''
                r=sr.Recognizer()
                text_dict = defaultdict(str)
                for i in range(len(path_list)):
                    #data, samplerate = soundfile.read(str(sol+path_list[i]))
                    # wav_path = sol+path_list[i]
                    # wavio.write(wav_path, data, fs ,sampwidth=2)
                    #soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
                    harvad=sr.AudioFile(str(sol+path_list[i]))
                    with harvad as source:
                        audio=r.record(source)
                    val=r.recognize_google(audio)

                    final_text += val
                    #res[str(i)] = val
                    text_dict[str(i)] = final_text

                print(final_text)

            #print(res)


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
                response_id=Response.objects.create(userid=request.user.id, service='Senti Audio',servicepaths=servicePaths,serviceLocation=json_response,responsedata=responseData).id
                print(response_id)
                print(Response.objects.get(id=response_id).serviceLocation)
                responseId=response_id
            


                
                

                return JsonResponse({'responseId':responseId, 'status': 200, 'message': 'File uploaded successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'File upload failed'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': 'Text is currupted, please  type valid  text', 'error': str(e)})
