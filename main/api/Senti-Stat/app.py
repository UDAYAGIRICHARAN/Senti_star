
from pywebio.input import *
from pywebio.output import *
import requests
from collections import defaultdict
import time 
from pywebio.output import put_html
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import argparse
from pywebio import start_server
import language_tool_python  

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import re

    
app = Flask(__name__)
my_tool = language_tool_python.LanguageTool('en-US')  



def task_func():

    name=input("Enter Your name",type="text",required=True)
    put_markdown("# Welcome,to Emorec Stats %s!! " %(name))




    def check(agree):
        if agree != ['I Agree to terms and conditions']:
            return 'Please agree to the terms and conditions'


    
    put_markdown(' ## Refer To Terms [Here](https://github.com/appdotnet/template-terms-of-service/blob/master/terms_template.md)')
    agree = checkbox("User terms and Conditions", options=['I Agree to terms and conditions'],validate=check)




    file = file_upload(label='Upload your text file', accept='.txt',required=True)
    content = file['content'].decode('utf-8').splitlines()

#     # Spell check 
#     new_doc = TextBlob(content)
#     result = new_doc.correct()
    
#     # Grammar correction 
#     content = my_tool.check(result)  
    
#     # Data cleaning pipeline
#     sol = []
#     for sentence in content: 
#         # Tokenisation
#         words=word_tokenize(sentence)


#         # Remove punctuations
#         filtered_text=[word for word in text if word not in string.punctuations]
#         sentence = ''.join(filtered_text)
        
        
#         # Removing emojt's
#         emoji pattern= re.compile("["

#         u"\U0001F600-\U0001F64F" # emoticons

#         u"\U0001F300-\U0001F5FF" # symbols & pictographs

#         u"\U0001F680-\U0001F6FF" # transport & map symbols

#         u"\U0001F1E0-\U0001F1FF" # flags (tos)
#         "]+", flags=re.UNICODE)

#         text=emoji pattern.sub(r'', text)

#         # Removeing HTML Tags
#         CLEANR = re.compile('<.*?>]&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});") 
#         cleantext = re.sub(CLEANR, text) 

#         #Removing url's
#         URLless_string = re.sub('\w+:\/{2}{\d\w-}+{\.[\d\w-]+)*(?: (?:\/[^\s/]*))*, text)  
#         text=URLless_string

#         # Remove numbers
#         no_digits = []
#         for i in text:
#             if not i.isdigit():
#                 no_digits.append(t)
#         final_result.join(no_digits)

#         # Transformed text     
#         sentence = ''
#         sentence += final_result


#         # Stopwords removal
#         words=word_tokenize(sentence) 
#         stop_words = set(stopwords.words('english'))
#         filtered_sentence=[]
#          for word in words:
#               if word not in stop_words:
#                   filtered_sentence.append(word)
#         text =  ''.join(filtered_sentence)



#         # POS TAGGING 
#         words=word_tokanize(text) 
#         final_result=""
#         removable_words=['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$', 'WP', 'WP$'] 
#         parts_of_speach_tag=nltk.pos_tag(words)

#         for word in parts_of_speach_tag:
#             if word[1] not in removable_words:
#                 final_result+=word[0]

#         sol.append(final_result)
                                
                                
#    content = sol




               
                            
    # further API code
    with put_loading(shape='grow',color='primary'):
        time.sleep(5)

        dic = defaultdict(lambda:0)
        for i in range(len(content)):
            query = {'text':str(content[i])}
            response = requests.get('https://detect-emotionapi.herokuapp.com/sentiment_analysis/', params=query)
            dic[response.json()]+=1



        Reviews= list(dic.keys())
        values = list(dic.values())


        put_markdown("## Table Here : ")
        fig = go.Figure(data=[go.Table(header=dict(values=['Reviews', 'Count']),cells=dict(values=[Reviews, values]))])
        html = fig.to_html(include_plotlyjs="require", full_html=False)
        put_html(html)




        put_markdown("## Bar Chart Here : ")
        fig = go.Figure([go.Bar(x=Reviews, y=list(dic.values()))])
        html = fig.to_html(include_plotlyjs="require", full_html=False)
        put_html(html)
 



        put_markdown('## Pie Chart Here : ')
        fig = go.Figure(data=[go.Pie(labels=Reviews, values=values)])
        html = fig.to_html(include_plotlyjs="require", full_html=False)
        put_html(html)



        put_markdown('## Donut Chart Here: ')
        fig = go.Figure(data=[go.Pie(labels=Reviews, values=values, hole=.3)])
        html = fig.to_html(include_plotlyjs="require", full_html=False)
        put_html(html)

        put_markdown('## Horizontal Bar Chart Here : ')
        fig = go.Figure(go.Bar(x=values,y=Reviews,orientation='h'))
        html = fig.to_html(include_plotlyjs="require", full_html=False)
        put_html(html)




        put_markdown('## Pulled Donut Chart Here: ')
        fig = go.Figure(data=[go.Pie(labels=Reviews, values=values, pull=[0, 0, 0.2, 0])])
        html = fig.to_html(include_plotlyjs="require", full_html=False)
        put_html(html)




app.add_url_rule('/tool', 'webio_view', webio_view(task_func),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(task_func, port=args.port)
