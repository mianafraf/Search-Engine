import csv


class generate:
      
    def __init__(self):
     f=open('index.txt','r')
     data=f.readline()
     lis=data.split(",")
     self.wid=int(lis[0])
     self.did=int(lis[1])
     self.lexicon={}
     self.doc={}
     f.close()
  
        
    def loadlexicon(self):
     with open('lexicon.csv','r') as data:
      for line in csv.reader(data):
            k,d=line
            self.lexicon[k]=d
    
    def savelexicon(self):
     with open('lexicon.csv', 'w') as f:
      for key in self.lexicon.keys():
        f.write("%s,%s\n"%(key,self.lexicon[key]))
    

    def generatelexicon(self,arr):
     for i in arr:
       if len(i[0])>1:
        word=i[0]
        if word in self.lexicon.keys():
        #generate forward index here
         pass
        else:
         self.wid=self.wid+1
         self.lexicon[word]=self.wid
         self.generatelexicon(word)

    def saveindex(self):
      f=open('index.txt','w')
      f.write("%d,%d\n"%(self.wid,self.did))
      
      
