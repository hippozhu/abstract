import sys, re, glob, string, os
from nltk.corpus import stopwords
from nltk import word_tokenize
from abstract import *

#news_dirpath = '/home/yzhu7/data/tipster/wsj'
news_dirpath = sys.argv[1]
news_files = [os.path.join(root, f) for root, dir, files\
in os.walk(news_dirpath) for f in files if f.startswith('la')]
print len(news_files)
fout = open(sys.argv[2], 'w')
for i, news_file in enumerate(news_files):
  matches = re.findall(r'<TEXT>(.*?)</TEXT>',\
  re.sub('\n', ' ', open(news_file).read()))
  fout.write('\n'.join([remove_punctuation(match).lower() for match in matches]) + '\n')
  if (i+1)%10 == 0:
    print i+1
fout.close()
