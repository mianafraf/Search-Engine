import csv
from generate import generate

v=generate()
v.wid=0
v.saveindex()
f=open('lexicon.csv','w')

f.close()

v.loadfindex()
print(v.findex)
v.savefindex()
f=open('forwardindex.csv','w')


