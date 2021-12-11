import pandas as pd
import csv
#from generate.py import generate

#parsing json file to pd dataframe
df = pd.read_json('nela-covid-2020/newsdata/21stcenturywire.json')

#initializes dictionary where key is a word in the article
#the values for each key are the positions at which they occur in the doc
#number of occurences can be obtained by using len() 



for item in range(0,len(df.index)):
    occ_dict = {}
    #obtaining content from dataframe
    #placing content in array
    words = df['content'][item].split()

    #code for getting indices of words
    for index,word in enumerate(words):

        if len(word)>2:
            if word in occ_dict.keys():

                occ_dict[word].append(index)
            else:
                occ_dict[word] = []
                occ_dict[word].append(index)

    #lex_gen = generate() 
