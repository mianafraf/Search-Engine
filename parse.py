import pandas as pd
import csv
from generate import generate
import os
print(os.getcwd())
v=generate()

#basePath = os.path.dirname(os.path.abspath(__file__))
basePath=os.getcwd()
#df = pd.read_json(basePath + '/nela-covid-2020/newsdata/21stcenturywire.json')
df=pd.read_json(open('21stcenturywire.json', "r", encoding="utf-8"))
#parsing json file to pd dataframe
#df = pd.read_json('nela-covid-2020/newsdata/21stcenturywire.json')

#initializes dictionary where key is a word in the article
#the values for each key are the positions at which they occur in the doc
#number of occurences can be obtained by using len() 


print("welcome")


for item in range(0,len(df.index)):
    occ_dict = {}
    #obtaining content from dataframe
    #placing content in array
    words = df['content'][item].split()
    title=df['title'][item]
    url=df['url'][item]

    #code for getting indices of words
    v.loadlexicon()
    v.loadfindex()
    v.loadinvindex()
    #v.loaddocids()
    i=0
    for index,word in enumerate(words):

        if len(word)>2:
            if word in occ_dict.keys():

                occ_dict[word].append(index)
            else:
                occ_dict[word] = []
                occ_dict[word].append(index)
    
    
    v.generatelexicon(occ_dict,title,url)
    #if(i==0):print(occ_dict)
    i=i+1
    print(i)
    print(v.doc)
    v.savelexicon()
    v.savefindex()
    v.saveinvindex()
    v.savedocids()
    v.saveindex()