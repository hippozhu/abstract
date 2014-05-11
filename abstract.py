import sys, re, glob, string, os
from time import time
from nltk.corpus import stopwords
from nltk import word_tokenize

regex_punc = re.compile('[%s]' % re.escape(string.punctuation))
stopwordlist = stopwords.words('english')

# clean up tags, html escape chars
def clean_escape_char(text):
  if text == None:
	return ''
  text = ''.join(i if i in string.printable else ' ' for i in text)
  text = re.sub('&amp;', u'&', re.sub('&gt;', u'>', re.sub('&lt;', u'<', text)))
  text = re.sub('<[^>]*>', u' ', text)
  #text = re.sub('\n|&\w+;|&#\d+;', u' ', text)
  text = re.sub('\n|&\w+;|&#\w+;', u' ', text)
  return text.lower().encode('utf-8')

def clean_escape_char_nolower(text):
  if text == None:
	return ''
  text = ''.join(i if i in string.printable else ' ' for i in text)
  text = re.sub('&amp;', u'&', re.sub('&gt;', u'>', re.sub('&lt;', u'<', text)))
  text = re.sub('<[^>]*>', u' ', text)
  text = re.sub('\n|&\w+;|&#\w+;', u' ', text)
  return text.encode('utf-8')

def remove_punctuation(text):
  text = ''.join(i if i in string.printable else ' ' for i in text)
  return regex_punc.sub(' ', text)

def tokenize(text):
  #text = clean_escape_char(text)
  text = remove_punctuation(text).lower()
  return word_tokenize(text)
  
def tokenize_nostopword(text):
  #text = clean_escape_char(text)
  text = remove_punctuation(text).lower()
  return [token for token in word_tokenize(text) if token not in stopwordlist]

if __name__ == '__main__':
  #dirpath = '/home/yzhu7/git/abstract/tipster/'
  #texts = [os.path.join(root, f) for root, dir, files in os.walk(dirpath) for f in files if f.endswith('.txt')]
  #print len(abstracts)
  fout = open('all.txt', 'w')
  for i, line in enumerate(open('all')):
    fout.write(' '.join(tokenize(line.strip())) + '\n')
    if (i+1)%1000 == 0:
      print i+1
  fout.close()
