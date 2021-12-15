from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from generate import generate
import os
print(os.getcwd())

#basePath = os.path.dirname(os.path.abspath(__file__))
basePath = os.getcwd()
#df = pd.read_json(basePath + '/nela-covid-2020/newsdata/21stcenturywire.json')
df = pd.read_json(open('21stcenturywire.json', "r", encoding="utf8"))
# parsing json file to pd dataframe
#df = pd.read_json('nela-covid-2020/newsdata/21stcenturywire.json')

# initializes dictionary where key is a word in the article
# the values for each key are the positions at which they occur in the doc
# number of occurences can be obtained by using len()

v = generate()
print("start")

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()

for item in range(0, len(df.index)):
    occ_dict = {}
    # obtaining content from dataframe
    # placing content in array
    words = df['content'][item].split()

    # code for getting indices of words
    v.loadlexicon()
    i = 0
    for index, word in enumerate(words):
        if len(word) > 1:
            if word not in stop_words:
                emptyString = ""
                word = word.lower()
                if word.isalpha():
                    for character in word:
                        if character.isalnum():
                            emptyString += character
                        else:
                            emptyString += " "
                    pos = pos_tag([word])
                    print(lemmatizer.lemmatize(word, pos))
                    if word in occ_dict.keys():
                        occ_dict[word].append(index)
                    else:
                        occ_dict[word] = []
                        occ_dict[word].append(index)

                key_iterable = occ_dict.keys()
                key_list = list(key_iterable)
                v.generatelexicon(key_list)
            else:
                break
    # if(i==0):print(occ_dict)
    i = i+1
    v.savelexicon()
    v.saveindex()

print("stop")