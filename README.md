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




EXPERIMENTAL RESULTS



       Confusion Matrix






Accuracy : 1274 / 1500
=
85%
Recall : 802 / ( 802 + 118)
=
87%
Precision : 802 / (802 + 108)
=
88%




Screenshots
1)Home page :


EXPERIMENTAL RESULTS



       Confusion Matrix






Accuracy : 1274 / 1500
=
85%
Recall : 802 / ( 802 + 118)
=
87%
Precision : 802 / (802 + 108)
=
88%




Screenshots
1)Home page :





2)login page :





3)History page :











4)Senti files :






    5)Senti Type :




 6)Senti Image :












7)Senti Trans :



8)Senti Audio :









9)Senti URL :










CONCLUSION

In conclusion, sentiment analysis, also known as opinion mining, involves the examination of people's attitudes, emotions, and sentiments towards particular entities. This study focuses on the essential aspect of sentiment analysis, namely sentiment polarity categorization. Our research utilizes data from online product reviews on Amazon.com. We have developed a sentiment polarity categorization methodology and provided comprehensive explanations for each stage of the process. We have conducted experiments to evaluate the effectiveness of both sentence-level and review-level categorization.




         

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





2)login page :





3)History page :











4)Senti files :






5)Senti Type :




 6)Senti Image :












7)Senti Trans :



8)Senti Audio :









9)Senti URL :










CONCLUSION

In conclusion, sentiment analysis, also known as opinion mining, involves the examination of people's attitudes, emotions, and sentiments towards particular entities. This study focuses on the essential aspect of sentiment analysis, namely sentiment polarity categorization. Our research utilizes data from online product reviews on Amazon.com. We have developed a sentiment polarity categorization methodology and provided comprehensive explanations for each stage of the process. We have conducted experiments to evaluate the effectiveness of both sentence-level and review-level categorization.




         

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

