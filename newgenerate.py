import csv


class generate:
      
    def __init__(self):
        f=open('index.txt','r')
        data=f.readline()
        lis=data.split(",")
        self.wid=int(lis[0])
        self.did=int(lis[1])
        f.close()
        self.lexicon={} #dict containing lexicon
        self.doc=[] #list containing doc ids
        self.findex=[] #list containing forward index
     
  
        
    def loadlexicon(self):
        with open('lexicon.csv','r') as data:
            for line in csv.reader(data):
                k,d=line
                self.lexicon[k]=d
    
    def savelexicon(self):
        with open('lexicon.csv', 'w') as f:
            for key in self.lexicon.keys():
                f.write("%s,%s\n"%(key,self.lexicon[key]))
    
    # function iterates through every key in one document
    # checks if it is already in lexicon, otherwise assigns it a word id
    def generatelexicon(self,dictn):
        for key in dictn:
            word=key
            if word in self.lexicon.keys():
        #generate forward index here
                pass
            else:
                self.lexicon[word]=self.wid
                self.wid=self.wid+1

    def saveindex(self):
        f=open('index.txt','w')
        f.write("%d,%d\n"%(self.wid,self.did))


    def loadfindex(self):
        file = open("forwardindex.csv", "r")
        csv_reader = csv.reader(file)
        for row in csv_reader:
            self.findex.append(row)
   
    def savefindex(self):
        with open('forwardindex.csv', 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerows(self.findex)
      
     

    #def generatefindex(self,wid)
