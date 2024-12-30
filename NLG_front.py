import streamlit as st
import warnings
import nltk

paragraph=st.text_input('Enter a paragraph here:',value='This is the default value')             
# Cleaning the texts
import re # re libray will use for regular expression 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)

corpus = []

# Create the empty list name as corpus becuase after cleaned the data corpus will store this clean data

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
#   review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]   
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the Bag of Words model 

# Also we called as document matrix 
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X_bow = cv.fit_transform(corpus).toarray()


from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
X_tf = tf.fit_transform(corpus).toarray()
st.write('Data is converted into numbers:')
st.write(X_bow)
st.write('The numbers here are converted in the form of 0-1')
st.write(X_tf)

warnings.filterwarnings("ignore")
