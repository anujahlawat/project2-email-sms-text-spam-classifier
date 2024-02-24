email spam/ham classifier (feb 2024)

end to end project
In this project i am going to prepare a website and user/client will able to check if the typed message/email is spam/ham.



1. It is a machine learning classification project.
2. data set is taken from "uci Machine Learning".
   Almeida,Tiago and Hidalgo,Jos. (2012). SMS Spam Collection. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84.
2. i create a website and machine learning model works in the backgroud in  
   a such a way that a user tell the text message or email and model will classify the message/mail as spam/not spam i.e. ham.

stages of project :
1. data cleaning
2. EDA (#data analysis)
3. text preprocessing
4. modelling (#machine learning models, #model evaluation)
5. model improvement
6. website
7. deployment

insights : 
1. data is imbalanced. only 12.63% records are spam. and in our real world 
   also, spam are less as compared to ham e.g. check your mail box.
2. no of characters, words and sentences are more in spam as compared to 
   ham messages.

observation :
i predict for some random msg/mail taken randomly from google and i find that model is doing really well.

result : 1)i use MultinomialNB because it give high precision value
         2)i get accuracy = 97.19 %
         3)i get precision = 100%
         4)obviously our model may predict wrongly because accuracy is still 97.19%


challenges/issues/limitations : 
1. i trained my model on small size dataset.
2. dataset is imbalanced. we need to check f1-score as we can't rely on     
   precision/accuracy only for imbalanced dataset.
3. our necessary condition for ham/spam problem is high precision score,
   but we cann't leave accuracy.

