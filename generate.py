import csv
import numpy as np

class generate:
      
    def __init__(self):
     f=open('index.txt','r')
     data=f.readline()
     lis=data.split(",")
     self.wid=int(lis[0])
     self.did=int(lis[1])
     f.close()
     self.i=0
     self.lexicon={} #dict containing lexicon
     self.doc=[] #list containing doc ids
     self.findex=[[[0]]] #list containing forward index
     

    def loadlexicon(self):
     with open('lexicon.csv','r') as data:
      for line in csv.reader(data):
            for i in range(len(line)):
             if(i==0):
              k=line[0]
             else:
              d=line[i]       
                  
            self.lexicon[k]=d
      data.close()      
    
    def savelexicon(self):
     with open('lexicon.csv', 'w') as f:
      for key in self.lexicon.keys():
        f.write("%s,%s\n"%(key,self.lexicon[key]))
      f.close()
    

  
     # function iterates through every key in one document
    # checks if it is already in lexicon, otherwise assigns it a word id
    def generatelexicon(self,dictn):
        self.did=self.did+1  
        #for i in range(len(dictn)):
        for key in dictn:
            word=key
            #word=dictn[i]
            word.replace(',','')
            if word in self.lexicon.keys():
                self.generatefindex(self.lexicon[word],dictn[word])
                #pass
            else:
             self.lexicon[word]=self.wid
             self.generatefindex(self.lexicon[word],dictn[word])
             self.wid=self.wid+1
             self.i=self.i+1

    def saveindex(self):
      f=open('index.txt','w',encoding="utf-8")
      f.write("%d,%d\n"%(self.wid,self.did))
      f.close()


    def loadfindex(self):
     counter=0 #count number of rows     
     file = open("forwardindex.csv", "r")
     csv_reader = csv.reader(file)
     
     count=0 #count variable 

     for row in csv_reader:
      if(counter==0):
        self.findex = [[[int(row[1])]]]   
        counter=1;  
 
   
      for i in range(len(row)):
        if(i==0):   
          if(int(row[i])+1>len(self.findex) and counter == 2):       
            self.findex.append([[int(row[i+1])]]) #a new for next docid is appended
            count=0

          elif(counter==2):
            self.findex[int(row[i])].append([int(row[i+1])]) #a new 1d list for next wordid is appended
            count=count+1
        elif(i>1):
          self.findex[int(row[0])][count].append(int(row[i]))
      
      counter=2
     file.close()    
   
    def savefindex(self):
     file = open('forwardindex.csv', 'w', newline ='\n')
  
     #writing the data into the file
     with file:    
       write = csv.writer(file)
       for i in range(len(self.findex)):   
         for j in range(len(self.findex[i])):
           xz=[i]
             
           for k in range(len(self.findex[i][j])):
             xz.append(self.findex[i][j][k])
           write.writerow(xz)
     file.close()
      
     
    def adddoc(self):
     f=open('documents.txt','a')
     f.write("%d\n"%(self.did))
     f.close
     

    def generatefindex(self,id,listn):
      
       if(self.did+1>len(self.findex)):    
            self.findex.append([[id]])
       else: 
            self.findex[self.did].append([id])

       x=self.did
       try:
        y=len(self.findex[self.did])-1
       except:
            self.findex.append([[id]])
            y=len(self.findex[self.did])-1
       print(x,y)
       for i in range(len(listn)):
         self.findex[x][y].append(int(listn[i]))