# https://github.com/anujahlawat/project2-email-sms-text-spam-classifier.git

mport streamlit as st
import pickle            #it is required to import tfidf.pkl and vectorizer.pkl files
                         #need to install sklearn so that pickle can work
import string
from nltk.corpus import stopwords
import nltk
import spacy
nlp = spacy.load('en_core_web_sm')


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def transform_text(text):
    text = text.lower()                  #converting to lower case
    text = nltk.word_tokenize(text)      #tokenization 
    
    
    y=[]                                 #removing punctuation, special symbols, emoji, hyperlinks, mail id
    for i in text:                       #new line terminator \n, #tag, @mention. 
        if i.isalnum():
            y.append(i)
    text = y.copy()
    y.clear()
    
    
    for i in text:                        #removing stopwords
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y.copy()
    text = ' '.join(str(e) for e in text) #taking out elements from the list and join them
    y.clear()
    
    
    
    for i in nlp(text):                   #lemmatisation of words          
        y.append(i.lemma_)
    text = y.copy()
    y.clear()
    text = ' '.join(str(e) for e in text)  
    
    return text


st.title("mail/sms/text spam classifier")
input_data = st.text_area("enter the mail/sms/text")

if st.button('predict'):
    
    #now for the entered text, we have to perform these task
    #1. text preprocessing
    transformed_input = transform_text(input_data)

    #2. vectorizer
    vector_input = tfidf.transform([transformed_input])

    #3. predict the input
    result = model.predict(vector_input)[0]            #extracting zeroth item

    #4. display the result
    if result == 1:
        st.header("spam")
    else:
        st.header("ham")