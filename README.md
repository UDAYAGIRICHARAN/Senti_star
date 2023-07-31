#Senti Star


## TechstacK: 
frontend:React
Backend: Django
Database: Postgres


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




EXPERIMENTAL RESULTS



       Confusion Matrix






# Accuracy : 1274 / 1500
# =
# 85%
Recall : 802 / ( 802 + 118)
=
87%
Precision : 802 / (802 + 108)
=
88%




Screenshots
1)Home page :


EXPERIMENTAL RESULTS




```

Accuracy : 1274 / 1500
=
85%
Recall : 802 / ( 802 + 118)
=
87%
Precision : 802 / (802 + 108)
=
88%

```


# Screenshots

1)Home page :
![WhatsApp Image 2023-07-31 at 13 58 53](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/706f1dd0-ba8c-43a4-b813-1972a25b9c8e)



2)login page :


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/ca761ecb-3490-4891-8eeb-b24ec53914cc)


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/4deabe8c-fcab-48e9-98f7-66e1ac40c88a)


3)History page :

![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/37cd03df-a0be-4653-8448-d15ffbd2bdd5)










4)Senti files :


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/fef1004e-8240-47ff-8da0-36240bd8fb7c)


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/35816f81-71d1-4b0f-974f-b7f769693252)


5)Senti Type :

![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/19362306-ffa7-4584-b3e5-77525a696f4e)



 6)Senti Image :


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/b32e6f07-9010-4521-b511-2bd8ba182c68)


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/429890ff-2954-4ad8-9596-1a154b5b58cf)








7)Senti Trans :


![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/d323ff6a-33ad-4838-b980-aa97dc72f78d)

8)Senti Audio :




![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/e4411631-49e7-4928-be22-f56f74675216)

![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/c53ddbe3-e3da-408e-990b-4da3ba3e78ca)




9)Senti URL :



![WhatsApp Image 2023-07-31 at 13 58 53](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/e1990c6b-6478-4491-89d7-dc265382f6b5)

![WhatsApp Image 2023-07-31 at 13 58 54](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/908ac8ab-1953-4afb-a3d0-7e85010a64f2)


![WhatsApp Image 2023-07-31 at 13 58 54](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/14aa2865-9c28-4ebe-af7d-c2cb0d100623)


![WhatsApp Image 2023-07-31 at 13 58 55](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/8f9c33e1-db62-4c6c-b620-92d5c813907d)

![WhatsApp Image 2023-07-31 at 13 58 55](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/363b6e0a-b9ad-4278-8c89-318a5bf06794)



# Result page

![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/65ad5238-e9a0-45cc-acf6-e5395e073a8a)
![image](https://github.com/UDAYAGIRICHARAN/Senti_star/assets/67089878/19d00085-1645-4a27-944e-b54d21148b20)


         

FUTURE WORK


The future work on this will include Integrating this project with several other domains like Identifying and Predicting Market Trends, Keeping an eye on the brand’s image, Examining public opinion polls and political polls, Data from customer feedback is being analyzed, Observing and analyzing conversations on social media, Employee Turnover Reduction and Many More.

Real-time API
Deploy the Whole Application
Integrate with GPT-4 for better accuracy


REFERENCES

[1].Feldman, Ronen. "Techniques and applications for sentiment analysis." Communications of the ACM 56, no. 4 (2013): 82-89.
 
[2]. Kiritchenko, Svetlana, Xiaodan Zhu, and Saif M. Mohammad. "Sentiment analysis of short informal texts." Journal of Artificial Intelligence Research 50 (2014): 723-762.
 
[3]. Baek, Y., Lee, B., Han, D., Yun, S., & Lee, H. (2019). Character Region Awareness for Text Detection. ArXiv. https://doi.org/10.48550/arXiv.1904.01941 

[4]. Kirange, D. K., and R. R. Deshmukh. "Emotion classification of news headlines using SVM." Asian Journal of Computer Science and Information Technology 5, no. 2 (2012): 104-106.

[5].Alotaibi, Fahad Mazaed. "Classifying text-based emotions using logistic regression." (2019). 

[6].harupa, Nazia Anjum, et al. "Emotion detection of the Twitter post using multinomial Naive Bayes." 2020 11th International Conference on Computing, Communication and Networking Technologies (ICCCNT). IEEE, 2020.
[7].Le, Anh Duc, Dung Van Pham, and Tuan Anh Nguyen. "Deep learning approach for receipt recognition." Future Data and Security Engineering: 6th International Conference, FDSE 2019, Nha Trang City, Vietnam, November 27–29, 2019, Proceedings 6. Springer International Publishing, 2019.

[8].Zhang, Zixing, et al. "Deep learning for environmentally robust speech recognition: An overview of recent developments." ACM Transactions on Intelligent Systems and Technology (TIST) 9.5 (2018): 1-28.

[9].Harár, Pavol, Radim Burget, and Malay Kishore Dutta. "Speech emotion recognition with deep learning." 2017 4th International conference on signal processing and integrated networks (SPIN). 

[10].Chong, Wei Yen, Bhawani Selvaretnam, and Lay-Ki Soon. "Natural language processing  for sentiment analysis: an exploratory analysis on tweets." 2014 4th international conference on artificial intelligence with applications in engineering and technology. 

[11].Narayanan, Vivek, Ishan Arora, and Arjun Bhatia. "Fast and accurate sentiment classification using an enhanced Naive Bayes model." Intelligent Data Engineering and Automated Learning–IDEAL 2013: 14th International Conference, IDEAL 2013, Hefei, China, October 20-23, 2013. Proceedings 14. Springer Berlin Heidelber
