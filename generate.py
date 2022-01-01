import csv
import time

class generate:

    def __init__(self):
        f = open('E:/NUST/BSCS-10ABC/DSA/FINAL PROJECT/nela-covid-2020/index.txt', 'r')
        data = f.readline()
        lis = data.split(",")
        self.wid = int(lis[0])
        self.did = int(lis[1])
        f.close()
        self.ct = 0
        self.lexicon = {}  # dict containing lexicon
        self.doc = [[0]]  # list containing doc ids
        self.findex = [[[0]]]  # list containing forward index
        self.invindex = [[0]]  # list containing inverted index
        self.filesread = {}

    def loadlexicon(self):
        with open('lexicon.csv', 'r') as data:
            for line in csv.reader(data):
                for i in range(len(line)):
                    if (i == 0):
                        k = line[0]
                    else:
                        d = line[i]

                self.lexicon[k] = d
            data.close()

    def savelexicon(self):
        with open('lexicon.csv', 'w') as f:
            for key in self.lexicon.keys():
                f.write("%s,%s\n" % (key, self.lexicon[key]))
            f.close()

        # function iterates through every key in one document

    # checks if it is already in lexicon, otherwise assigns it a word id
    def generatelexicon(self, dictn, title, url):
        self.did = self.did + 1
        self.assigndocids(title, url)
        # for i in range(len(dictn)):
        for key in dictn:
            word = key
            # word=dictn[i]
            word.replace(',', '')
            if word in self.lexicon.keys():
                self.generatefindex(self.lexicon[word], dictn[word])
                self.generateinvindex(int(self.lexicon[word]))
                # pass
            else:
                self.lexicon[word] = self.wid
                self.generatefindex(self.lexicon[word], dictn[word])
                self.generateinvindex(int(self.lexicon[word]))
                self.wid = self.wid + 1

    def saveindex(self):
        f = open('index.txt', 'w', encoding="utf-8")
        f.write("%d,%d\n" % (self.wid, self.did))
        f.close()

    def loadfindex(self):
        counter = 0  # count number of rows     
        file = open("forwardindex.csv", "r")
        csv_reader = csv.reader(file)

        count = 0  # count variable 

        for row in csv_reader:
            if (counter == 0):
                self.findex = [[[int(row[1])]]]
                counter = 1

            for i in range(len(row)):
                if (i == 0):
                    if (int(row[i]) + 1 > len(self.findex) and counter == 2):
                        self.findex.append([[int(row[i + 1])]])  # a new for next docid is appended
                        count = 0

                    elif (counter == 2):
                        self.findex[int(row[i])].append([int(row[i + 1])])  # a new 1d list for next wordid is appended
                        count = count + 1
                elif (i > 1):
                    self.findex[int(row[0])][count].append(int(row[i]))

            counter = 2
        file.close()

    def savefindex(self):
        file = open('forwardindex.csv', 'w', newline='\n')

        # writing the data into the file
        with file:
            write = csv.writer(file)
            for i in range(len(self.findex)):
                for j in range(len(self.findex[i])):
                    xz = [i]

                    for k in range(len(self.findex[i][j])):
                        xz.append(self.findex[i][j][k])
                    write.writerow(xz)
        file.close()

    def adddoc(self):
        f = open('documents.txt', 'a')
        f.write("%d\n" % (self.did))
        f.close

    def generatefindex(self, id, listn):  # takes wid as an argument

        if (self.did == 0 and id == 0):
            self.findex = [[[id]]]
            self.ct = 1

        if (self.did + 1 > len(self.findex)):
            self.findex.append([[id]])
            self.ct = 1
        else:
            if (self.did != 0 or (self.did == 0 and id != 0)):
                self.findex[self.did].append([id])

        x = self.did
        try:
            y = len(self.findex[self.did]) - 1
        except:
            self.findex.append([[id]])
            y = len(self.findex[self.did]) - 1
        # print(x,y)
        for i in range(len(listn)):
            self.findex[x][y].append(int(listn[i]))
        self.ct = 2

    def loadinvindex(self):
        counter = 0
        count = 0
        f = open('invertedindex.csv', 'r')

        csv_reader = csv.reader(f)

        for row in csv_reader:
            if (counter == 0):
                self.invindex = [[int(row[0])]]
                counter = 1
            for i in range(len(row)):
                if (i == 0 and counter == 2):
                    self.invindex.append([int(row[0])])
                    count = count + 1
                elif (i > 0):
                    self.invindex[count].append(int(row[i]))

            counter = 2
        f.close()

    
    def getoccurrences(self,wordid,docid):
        occurrences = 0
        document = self.findex[docid]
        for wordlist in document:
            if wordlist[0] == wordid:
                occurrences = len(wordlist[1:])   

        return occurrences                

    def mergesortdoclist(self,wordid, doclist):
        if len(doclist) > 1:
            mid = len(doclist)//2
  
            # Dividing the array elements
            left = doclist[:mid]
    
            # into 2 halves
            right = doclist[mid:]

            self.mergesortdoclist(wordid,left)

            self.mergesortdoclist(wordid,right)

            i = j = k = 0
  
            # Copy data to temp arrays L[] and R[]
            while i < len(left) and j < len(right):
                if self.getoccurrences(wordid,left[i])  > self.getoccurrences(wordid,right[j]):
                    doclist[k] = left[i]
                    i += 1
                else:
                    doclist[k] = right[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(left):
                doclist[k] = left[i]
                i += 1
                k += 1
    
            while j < len(right):
                doclist[k] = right[j]
                j += 1
                k += 1
    
    
    def countsortdoclist(self,wordid,doclist):
        # The output character array that will have sorted arr
        output = [0 for i in range(len(doclist))]
    
        # Create a count array to store count of individual
        # characters and initialize count array as 0
        count = [0 for i in range(len(doclist))]
    
       
    
        # Store count of each character
        for i in range(0,len(doclist)):
            count[i] = self.getoccurrences(wordid,doclist[i])
        print (count)
        
        for i in range(0,len(doclist)):
            output[i] = doclist[count.index(max(count))]
            doclist.remove(doclist[count.index(max(count))])
            count.remove(max(count))
       
    
        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(output)):
            doclist.append(output[i])
        

            
            
    
    
    
    def insertionSort(self,wordid,doclist):
 
        # Traverse through 1 to len(arr)
        for i in range(1, len(doclist)):
    
            key = doclist[i]
    
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and self.getoccurrences(wordid,key) > self.getoccurrences(wordid,doclist[j]) :
                    doclist[j + 1] = doclist[j]
                    j -= 1
            doclist[j + 1] = key
    
    
    
    def sortfullinvindex(self):
        for wordid, doclist in enumerate(self.invindex):
            start = time.time()
            print(wordid)
            # self.insertionSort(wordid,doclist)
            # self.countsortdoclist(wordid,doclist)
            self.mergesortdoclist(wordid,doclist)
            print(time.time() - start)
            


        # for word_id, word_id_doc_list in enumerate(self.invindex):

        #     if len(word_id_doc_list)>1:
        #         mid = len(arr)//2
  
        #         # Dividing the array elements
        #         left = arr[:mid]
        
        #         # into 2 halves
        #         right = arr[mid:]


        #             for i in range(0,len(word_id_doc_list)-1):
        #                 if self.getoccurrences(word_id,word_id_doc_list[i]) < self.getoccurrences(word_id,word_id_doc_list[i+1]):
        #                     temp = word_id_doc_list[i]
        #                     word_id_doc_list[i] = word_id_doc_list[i+1]
        #                     word_id_doc_list[i+1] = temp
                            

        
        
    
    
    def saveinvindex(self):
        file = open('invertedindex.csv', 'w', newline='\n')

        # writing the data into the file
        with file:
            write = csv.writer(file)
            for i in range(len(self.invindex)):
                write.writerow(self.invindex[i])

        file.close()

    def generateinvindex(self, id):
        self.loadfindex()
        global occlist
        global num_of_occ
        num_of_occ = 0
        occlist = []
        if (self.wid == 0 and self.did == 0):
            pass  # do nothing

        else:
            
            
            if (id + 1 > len(self.invindex)):
                self.invindex.append([self.did])
                
                
            else:
                self.invindex[id].append(self.did)
                #code to sort inverted index while inserting
                # insert_occurrences = 0
                # dcid = self.findex[self.did]
                # for wordlist in dcid:
                #     if wordlist[0] == id:
                #          insert_occurrences = len(wordlist[1:])
                # for i, document in enumerate(self.invindex[id]):
                #     current_occurrences = 0
                #     dcid = self.findex[document]
                #     for wordlist in dcid:
                #         if wordlist[0] == id:
                #             current_occurrences = len(wordlist[1:])
                #     if insert_occurrences >= current_occurrences:
                #         self.invindex[id].insert(i,self.did)
                #         break        
                      
                

    def savedocids(self):
        file = open('docids.txt', 'w', newline='\n')

        for i in range(len(self.doc)):
            file.write(self.doc[i][0] + '\n')
            # file.write('\n')
            file.write(self.doc[i][1] + '\n')
            # file.write('\n')

        file.close()

    def loaddocids(self):
        counter = 0
        count = 0
        signal = 0
        f = open('docids.txt', 'r')
        Lines = f.readlines()

        for line in Lines:
            if (counter == 0):
                lin = line.rstrip('\n')
                self.doc = [[lin]]
                counter = 1
                signal = 1
            else:
                if signal == 0:
                    lin = line.rstrip('\n')
                    self.doc.append([lin])
                    count = count + 1
                    signal = 1
                else:
                    lin = line.rstrip('\n')
                    self.doc[count].append(lin)
                    signal = 0
        f.close()

    def assigndocids(self, title, url):
        if (self.did == 0):
            self.doc = [[title]]
            self.doc[self.did].append(url)
        else:
            self.doc.append([title])
            self.doc[self.did].append(url)

    def savefilesread(self):
        a_file = open("filesread.csv", "w")
        writer = csv.writer(a_file)
        for key, value in self.filesread.items():
            writer.writerow([key, value])

        a_file.close()
        self.filesread = {}

    def loadfilesread(self):
        with open('filesread.csv', 'r') as data:
            for line in csv.reader(data):
                for i in range(len(line)):
                    if (i == 0):
                        k = line[0]
                        # d = ''
                    else:
                        d = line[i]

                self.filesread[k] = d
        data.close()
    