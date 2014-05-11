from sklearn.svm import LinearSVC
from gensim.models import Word2Vec
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from abstract import *
from sklearn.datasets import fetch_20newsgroups
from nltk.corpus import stopwords
import numpy as np

categories = ['alt.atheism', 'talk.religion.misc','comp.graphics', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train',categories=categories, remove=('headers', 'footers', 'quotes'))
newsgroups_test = fetch_20newsgroups(subset='test',categories=categories, remove=('headers', 'footers', 'quotes'))

'''
vectorizer = TfidfVectorizer()
vectors_train = vectorizer.fit_transform(newsgroups_train.data)
vectors_test = vectorizer.transform(newsgroups_test.data)
clf = MultinomialNB(alpha=.01)
clf.fit(vectors_train, newsgroups_train.target)
pred = clf.predict(vectors_test)
print metrics.f1_score(newsgroups_test.target, pred)
'''

model_file = sys.argv[1]
#model = Word2Vec.load_word2vec_format('20news.ns.bin', binary=True)
model = Word2Vec.load_word2vec_format(model_file, binary=True)
tokens_train = [filter(lambda x: x in model.vocab and x not in stopwordlist, word_tokenize(remove_punctuation(msg).lower())) for msg in newsgroups_train.data]
tokens_test = [filter(lambda x: x in model.vocab and x not in stopwordlist, word_tokenize(remove_punctuation(msg).lower())) for msg in newsgroups_test.data]
vec_rep_train = np.array([np.array([model[token] for token in msg_tokens]).sum(axis=0) if len(msg_tokens)>0 else np.array([.0]*100) for msg_tokens in tokens_train])
vec_rep_test = np.array([np.array([model[token] for token in msg_tokens]).sum(axis=0) if len(msg_tokens)>0 else np.array([.0]*100) for msg_tokens in tokens_test])

clf = LinearSVC()
clf.fit(vec_rep_train, newsgroups_train.target)
pred = clf.predict(vec_rep_test)
print metrics.f1_score(newsgroups_test.target, pred)
