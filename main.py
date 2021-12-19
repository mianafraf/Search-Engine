from generate import generate

a=[[[2]]]
print(len(a))
print(len(a[0]))
print(len(a[0][0]))
a[0][0].append(4)
a[0].append(6)
print(a)

a=[['afra']]
print(a)
a[0].append("siyyab")
print(a)

ob=generate()
ob.loaddocids()
print(ob.doc)
for i in range(len(ob.doc)):

       # a=ob.doc[i][0].rstrip('\n')
        #b=ob.doc[i][1].rstrip('\n')
        #print(a)
        #print(b)
        print('\n')




f=open('lexicon.csv','w')
f.close()
f=open('index.txt','w')
f.write("%d,%d\n"%(0,-1))
f.close()
f=open('forwardindex.csv','w')
f.close()
f=open('invertedindex.csv','w')
f.close()
f=open('docids.txt','w')
f.close()
f=open('filesread.csv','w')
f.close()
#v= generate()
#v.loadfindex()
#print(v.findex)