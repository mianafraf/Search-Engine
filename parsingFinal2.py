import pandas as pd
from nltk.corpus import stopwords
from generate import generate
from nltk.stem import PorterStemmer
import time

v = generate()
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))    #creating class objects

filenames = []

filenames.append("yna.json")        #appending file in array to be parsed

v.loadfilesread()
v.loadlexicon()
v.loadfindex()
v.loadinvindex()
v.loaddocids()

print("start")      #indicates the file is running

i = 0
start = time.time()

for f in filenames:     #iterates over the number of files
  if f in v.filesread.keys():   #does not read the file which has already been read
    pass
  else:
    v.filesread[f] = 1
    
    df = pd.read_json(open(f, "r", encoding="utf8"))    #used to read the json file
    for item in range(0, len(df.index)):                #iterates till end-of-file is reached
        occ_dict = {}                                   #initialising the dictionary for each article
        words = df['content'][item].split()             
        title = df['title'][item]
        url = df['url'][item]                           #accessing respective columns of each article
        
        for index, word in enumerate(words):
            if len(word) > 1:
                if word not in stop_words:
                    if word.isalpha():
                        word = ps.stem(word)            #applying stemming function from NLTK library
                        if word in occ_dict.keys():     #if word has been read before, the additional index is appended
                            occ_dict[word].append(index)
                        else:      #if no key for the word is available, it is substituted with an empty array and index is appended anyway
                            occ_dict[word] = []
                            occ_dict[word].append(index)
        i = i+1                    #counting words to keep track
        print(i)
        if len(occ_dict.keys()) > 2:                #used to stay within range
            v.generatelexicon(occ_dict, title, url) #function generates lexicon using the dictionary created for the article
    print(f)                                        #prints file name
    v.savedocids()                                  #saves the document IDs
    if i > 100000:
        break

print(time.time() - start)

v.savelexicon()
v.savefindex()
v.saveindex()
v.saveinvindex()
v.savefilesread()                                   #functions executed to save all the data that has been read

print("stop")                                       #indicates file has been parsed