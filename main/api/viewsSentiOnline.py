from django.shortcuts import render
from django.http import JsonResponse
from .forms import UrlUploadForm
from .models import Url,Response
def senti_online(request):
    if request.user.is_authenticated:
        print(request.POST)
        if request.method == 'POST':
            form = UrlUploadForm(request.POST, request.FILES)
            print(form)

            if form.is_valid():
                urls = form.cleaned_data['url']
                userid = request.user.id
                #scrapping the text
                responseText = helper.scrapText(urls, userid)
               
                return render(request, 'pages/sentiUrl.html', {'path_list': path_list})
            else:
                return render(request, 'pages/sentiUrl.html', {'form': form})
        else:
            form = UrlUploadForm()
            return render(request, 'pages/sentiUrl.html', {'form': form})
    else:
        return redirect('login')

class helper:
    def scrapText(url, userid):
        #scraping the text from the url
        import requests
        from bs4 import BeautifulSoup
        #get the url
        url = url
        #get the response
        response = requests.get(url)
        #get the html
        html = response.text
        #parse the html
        soup = BeautifulSoup(html, 'html.parser')
        #get the text
        text = soup.get_text()










        #return the text
        return text
