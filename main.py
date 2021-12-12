from generate import generate

a=[[[2]]]
a[0][0].append(4)
a[0].append(6)
print(a)

f=open('lexicon.csv','w')
f.close()
f=open('index.txt','w')
f.write("%d,%d\n"%(0,-1))
f.close()
f=open('forwardindex.csv','w')
#v= generate()
#v.loadfindex()
#print(v.findex)