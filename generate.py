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
     self.ct=0
     self.lexicon={} #dict containing lexicon
     self.doc=[[0]] #list containing doc ids
     self.findex=[[[0]]] #list containing forward index
     self.invindex=[[0]] #list containing inverted index
    
     

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
    def generatelexicon(self,dictn,title,url):
        self.did=self.did+1 
        self.assigndocids(title,url) 
        #for i in range(len(dictn)):
        for key in dictn:
            word=key
            #word=dictn[i]
            word.replace(',','')
            if word in self.lexicon.keys():
                self.generatefindex(self.lexicon[word],dictn[word])
                self.generateinvindex(int(self.lexicon[word]))
                #pass
            else:
             self.lexicon[word]=self.wid
             self.generatefindex(self.lexicon[word],dictn[word])
             self.generateinvindex(int(self.lexicon[word]))
             self.wid=self.wid+1
             

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
     

    def generatefindex(self,id,listn): #takes wid as an argument

       if(self.did==0 and id==0):
         self.findex=[[[id]]]
         self.ct=1
       
       if(self.did+1>len(self.findex)):
           self.findex.append([[id]])
           self.ct=1          
       else:
          if(self.did !=0 or (self.did==0 and id!=0)):     
            self.findex[self.did].append([id])

       x=self.did
       try:
        y=len(self.findex[self.did])-1
       except:
            self.findex.append([[id]])
            y=len(self.findex[self.did])-1
       #print(x,y)
       for i in range(len(listn)):
         self.findex[x][y].append(int(listn[i]))
       self.ct=2

    def loadinvindex(self):
      counter=0
      count=0
      f=open('invertedindex.csv','r')

      csv_reader=csv.reader(f)

      for row in csv_reader:
        if(counter==0):
          self.invindex=[[int(row[0])]]
          counter=1
        for i in range(len(row)):
          if(i==0 and counter==2):
            self.invindex.append([int(row[0])])
            count=count+1
          elif(i>0):
            self.invindex[count].append(int(row[i]))    

        counter=2  
      f.close()     

    def saveinvindex(self):
      file = open('invertedindex.csv', 'w', newline ='\n')
  
     #writing the data into the file
      with file:    
        write = csv.writer(file)
        for i in range(len(self.invindex)):   
           write.writerow(self.invindex[i])
     
      file.close()

    def generateinvindex(self,id):
      if(self.wid==0 and self.did==0):
        pass #do nothing

      else:
         if(id+1>len(self.invindex)):
           self.invindex.append([self.did])
         else:
           self.invindex[id].append(self.did)    

    def savedocids(self):
          file = open('docids.txt', 'w', newline ='\n')

          for i in range(len(self.doc)):
                file.write(self.doc[i][0]+'\n')
                #file.write('\n')
                file.write(self.doc[i][1]+'\n')
                #file.write('\n')
     
          file.close() 
           
    def loaddocids(self):
      counter=0
      count=0
      signal=0
      f=open('docids.txt','r')
      Lines = f.readlines()
    
      for line in Lines:
         if(counter==0):
             self.doc=[[line]]
             counter=1
             signal=1
         else:
           if signal==0:
              self.doc.append([line])
              count=count+1
              signal=1
           else:
              self.doc[count].append(line)
              signal=0 
      f.close()  

    def assigndocids(self,title,url):
      if(self.did==0 ):
        self.doc=[[title]]
        self.doc[self.did].append(url)   
      else:
        self.doc.append([title]) 
        self.doc[self.did].append(url) 


       
  
