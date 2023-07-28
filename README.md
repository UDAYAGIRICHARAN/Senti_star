#Senti Star

OBJECTIVE

We Propose to built a gateway of sentiment analysis that capable of process
almost every file type whether image,audios, pdf,ppt,doc,Youtube comments, mails, Blogs, webssites,videos . etc , Our Webapp can come to
conclusion for even large amount of data with sentiment report within seconds.

The Objective of the Project is to solve problems in the space of Natural
Language Processing with help of automation and Machine Learning.

This Project will solve Problem of going through each reviews and getting the
emotion of the text.

Deliverables include Statistical Charts and Scores for Positivity and Negativity
of Text.

PROJECT DESCRIPTION

The Application consists of 6 Microservices integrated to a Main Data
Aggregator

The Flow is as Follows, User is Initially Authenticated and the Landed on
The Data Aggregator application. Where in They get 5 Different Features
for sentiment classification.

User Authentication : The Initial Phase of the Project ,This Module Deals

With User Login,Registration via integrations Like Google and Github

Data Aggregator : This Module is the Core application aggregates all
different Microservices. Built With Django and Maintains all the transitions
to Different Microservices via DataBase

Sent-Online : This Microservice deals with Detecting human emotions by
capturing Text online. Has a Separate Page to Take Input and Process it
further.

Senti-Mage :This Microservice deals with Detecting human emotions by
capturing Images online.This Module uses OCR (Optical Character
Recognition) for sentiment recognition and EmoRec API for Classification

Sent-File : This Microservice deals Rendering a Statistical Dashboard for
Input File. This Module supports different files like txt,pdf,csv,doc,docx .
This also comes with the option to download the Charts.

Senti-Trans : This Module Deals with Translating given text and then
analyses sentiment of text using EmoRe API.

Senti-Speech : This Microservice deals with Detecting human emotions
by capturing Speech online. Has a Page to upload that speech and
Detect the Sentiment.

Senti-Url: This Microservice handles the articles, Blogs,Urls and mail

,Its able scrape and parse the data from websites and gives Sentiment
