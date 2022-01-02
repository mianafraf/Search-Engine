import pandas as pd
from nltk.corpus import stopwords
from generate import gen
from nltk.stem import PorterStemmer
import time
import os

v = gen()
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))  # creating class objects

path = os.getcwd() + "/newsdata"
filenames = []

for f in os.listdir(path):
    filenames.append(f)

v.loadlexicon()
v.loadfindex()
v.loadinvindex()
v.loaddocids()
v.loadfilesread()

print("start")  # indicates the file is running

i = 0
start = time.time()

for f in filenames:  # iterates over the number of files
    if f in v.filesread.keys():  # does not read the file which has already been read
        pass
    else:
        v.filesread[f] = 1

        # used to read the json file
        df = pd.read_json(open(path + "/" + f, "r", encoding="utf8"))
        for item in range(0, len(df.index)):  # iterates till end-of-file is reached
            occ_dict = {}  # initialising the dictionary for each article
            words = df['content'][item].split()
            title = df['title'][item] # accessing respective columns of each article
            url = df['url'][item]

            for index, word in enumerate(words):
                if len(word) > 1:
                    if word not in stop_words:
                        if word.isalpha():
                            word = ps.stem(word) # applying stemming function from NLTK library
                            if word in occ_dict.keys():  # if word has been read before, the additional index is appended
                                occ_dict[word].append(index)
                            else:  # if no key for the word is available, it is substituted with an empty array and index is appended anyway
                                occ_dict[word] = []
                                occ_dict[word].append(index)
            i = i + 1  # counting words to keep track
            print(i)
            if len(occ_dict.keys()) > 2:
                v.generatelexicon(occ_dict, title, url)  # function generates lexicon using the dictionary created for the article
        print(f)  # prints file name

    if i > 100000:
        break

print(time.time() - start)

v.savelexicon()
v.savefindex()
v.saveindex()
v.saveinvindex()
v.savedocids()  # saves the document IDs
v.savefilesread()  # functions executed to save all the data that has been read

print("stop")  # indicates file has been parsed