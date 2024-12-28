import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import blankline_tokenize
from nltk.util import trigrams,bigrams,ngrams
#Tokenization
#Stemming
#Lemmatization
#Stopwords

s=st.text_input("Enter a string here:")
options=['Word Tokenization', 'Sentence Tokenization', 'Blank Line Tokenization', 'Bigrams', 'Trigrams', 'N-grams']
s_option = st.selectbox("Select an option from these",options)

out=[]
n_st=word_tokenize(s)
if(s_option=='Word Tokenization'):
    wt=word_tokenize(s)
    out=wt
elif(s_option=='Sentence Tokenization'):
    s_t=sent_tokenize(s)
    out=s_t
elif(s_option=='Blank Line Tokenization'):
    bl_t=blankline_tokenize(s)
    out=bl_t

elif(s_option=='Bigrams'):
    bg=list(bigrams(n_st))
    out=bg
elif(s_option=='Trigrams'):
    tg=list(trigrams(n_st))
    out=tg
elif(s_option=='N-grams'):
    ng=list(ngrams(n_st,4))
    out=ng
st.write(out)