import csv


class generate:

    def __init__(self, dindex, windex):
        self.dindex = dindex
        self.windex=windex

    def loadlexicon():
     lexicon={}
     with open('lexicon.csv','r') as data:
      for line in csv.reader(data):
            k,d=line
            lexicon[k]=d
     return lexicon
    
    def savelexicon(lexicon):
     with open('lexicon.csv', 'w') as f:
      for key in lexicon.keys():
        f.write("%s,%s\n"%(key,lexicon[key]))
    



   # def generatelexicon(a):
