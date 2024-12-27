import nltk
import nltk.corpus

# you can also create your own words
AI = '''Artificial Intelligence refers to the intelligence of machines. This is in contrast to the natural intelligence of
humans and animals. With Artificial Intelligence, machines perform functions such as learning, planning, reasoning and
problem-solving. Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines.
It is probably the fastest-growing development in the World of technology and innovation. Furthermore, many experts believe
AI could solve major challenges and crisis situations.'''

type(AI)

from nltk.tokenize import word_tokenize
AI_tokens=word_tokenize(AI)
# print(AI_tokens)
# print(len(AI_tokens))

from nltk.tokenize import sent_tokenize
AI_sent=sent_tokenize(AI)
# print(AI_sent)
# print(len(AI_sent))

from nltk.tokenize import blankline_tokenize
AI_blank=blankline_tokenize(AI)
# print(AI_blank)

from nltk.tokenize import WhitespaceTokenizer
wt=WhitespaceTokenizer().tokenize(AI)
# print(wt)

s="good apple cost $3.88 in hydrabad. Please buy two of them. Thanks."

from nltk.tokenize import wordpunct_tokenize
wo=wordpunct_tokenize(s)
# print(wo)

w_t=wordpunct_tokenize(AI)
# print(w_t)
# print(len(w_t))

from nltk.util import bigrams,trigrams,ngrams
string="Anuj patel this side it is a beutiful day everything is going till now and I am studying my class it's been more than 70 days now"
quote_tokens=nltk.word_tokenize(string)
# print(quote_tokens)
# print(len(quote_tokens))

q_bigram=list(nltk.bigrams(quote_tokens))
# print(q_bigram)
# print(len(q_bigram))

q_trigram=list(nltk.trigrams(quote_tokens))
# print(q_trigram)
# print(len(q_trigram))

# q_ngram=list(nltk.ngrams(quote_tokens,4))
# print(q_ngram)
# print(len(q_ngram))

q_ngram=list(nltk.ngrams(quote_tokens,6))
# print(q_ngram)
# print(len(q_ngram))

from nltk.stem import PorterStemmer
pst=PorterStemmer()

wordse_to_stem=['give','giving','given','gave','thinking','loving','maximum']

# for words in wordse_to_stem:
    # print(words+':'+pst.stem(words))
    
from nltk.stem import LancasterStemmer
lst=LancasterStemmer()
# for words in wordse_to_stem:
    # print(words+':'+lst.stem(words))

from nltk.stem import SnowballStemmer
sbs=SnowballStemmer('english')
# for words in wordse_to_stem:
#     print(words+':'+sbs.stem(words))

from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_len=WordNetLemmatizer()
# for words in wordse_to_stem:
#     print(words+':'+word_len.lemmatize(words))


from nltk.corpus import stopwords
# print(stopwords.words('english'))

s='anuj is natural when it comes to coding'
s_token=word_tokenize(s)
# for token in s_token:
    # print(nltk.pos_tag([token]))
    
from nltk import ne_chunk
ne_sent='the us presedent stays at white house'
ne_tokens=word_tokenize(ne_sent)
# print(ne_tokens)
ne_tags=nltk.pos_tag(ne_tokens)
print(ne_tags)

ne_ner=ne_chunk(ne_tags)
print(ne_ner)