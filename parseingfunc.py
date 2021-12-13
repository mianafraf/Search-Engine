import pandas as pd
import csv
# import nltk
# nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

v = generate()

# from generate.py import generate


# creating stemming object
ps = PorterStemmer()

# parsing json file to pd dataframe
df = pd.read_json('nela-covid-2020/newsdata/21stcenturywire.json')

# initializes dictionary where key is a word in the article
# the values for each key are the positions at which they occur in the doc
# number of occurences can be obtained by using len()


# range can be a maximim of len(df.index)
for item in range(0, len(df.index)):
    occ_dict = {}
    # obtaining content from dataframe
    # placing content in array
    words = df['content'][item].split()

    # code for getting indices of words
    v.loadlexicon()
    v.loadfindex()
    for index, word in enumerate(words):
        # converting word to lowercase
        word = word.lower()
        # removing non alphanumeric characters
        word = re.sub("[^0-9a-zA-Z-]+", ' ', word)
        # stemming word
        word = ps.stem(word)
        if len(word) > 0 and word not in stopwords.words('english'):
            if (word) in occ_dict.keys():

                occ_dict[(word)].append(index)
            else:
                occ_dict[(word)] = []
                occ_dict[(word)].append(index)

    key_iterable = occ_dict.keys()
    key_list = list(key_iterable)
    v.generatelexicon(occ_dict)
    v.savelexicon()
    v.savefindex()
    v.saveindex()
