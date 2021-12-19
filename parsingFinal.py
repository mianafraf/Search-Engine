from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tag import pos_tag
from generate import generate
from nltk.stem import PorterStemmer
import os
import time
from multiprocessing import pool

lemmatizer = WordNetLemmatizer()

#df = pd.read_json(basePath + '/nela-covid-2020/newsdata/21stcenturywire.json')
# parsing json file to pd dataframe
#df = pd.read_json('nela-covid-2020/newsdata/21stcenturywire.json')

# initializes dictionary where key is a word in the article
# the values for each key are the positions at which they occur in the doc
# number of occurences can be obtained by using len()

v = generate()
print("start")
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

path = "/Users/ahmadtashfeen/Downloads/dataverse_files/nela-covid-2020/newsdata"

filenames = []

for f in os.listdir(path):
    if f in v.filesread.keys():
        pass
    else:
        v.filesread[f] = 1
        filenames.append(f)

v.loadfilesread()
v.loadlexicon()
v.loadfindex()
v.loadinvindex()

i = 0
ac = 0

for f in filenames:
    v.loaddocids()
    start = time.time()
    df = pd.read_json(open(path + "/" + f, "r", encoding="utf8"))
    for item in range(0, len(df.index)):
        occ_dict = {}
        # obtaining content from dataframe
        # placing content in array
        words = df['content'][item].split()
        title = df['title'][item]
        url = df['url'][item]

        # code for getting indices of words
        
        for index, word in enumerate(words):
            if len(word) > 1:
                if word not in stop_words:
                    word = word.lower()
                    if word.isalpha():
                        word = ps.stem(word)
                        if word in occ_dict.keys():
                            occ_dict[word].append(index)
                        else:
                            occ_dict[word] = []
                            occ_dict[word].append(index)
        # if(i==0):print(occ_dict)
        i = i+1
        print(i)
        if len(occ_dict.keys()) > 2:
            v.generatelexicon(occ_dict, title, url)
    print(f)
    v.savedocids()
    if i > 100000:
        break

print(time.time() - start)

v.savelexicon()
v.savefindex()
v.saveindex()
v.saveinvindex()
v.savefilesread()

print("stop")
