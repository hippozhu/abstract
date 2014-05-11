from gensim.models import Word2Vec
import numpy as np

model = Word2Vec.load_word2vec_format('merged.bow.bin', binary=True)
texts = [line.strip().split() for line in open('bow.txt')]

def dissimilar(words, n):
  previous_word = None
  current_word = words[0]
  for i in xrange(n):
    previous_word = current_word
    ss = np.array([model.similarity(previous_word, x) for x in words])
    current_word = words[ss.argmin()]
  return previous_word, current_word

#def assign(clusters_sum, words):

def clustering(text):
  words = [t for t in text if t in model]
  #word_vec = np.array(model[w]

#if __name__ == '__main__':
