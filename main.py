from generate import generate
import csv

x=generate()
x.loadlexicon()
row,col=5,2
a = [[0 for i in range(col)] for j in range(row)]
for i in a:
 val=input("Enter word: ")
 print(val)
 i[0]=val

print(a)
x.generatelexicon(a)
x.savelexicon()
x.saveindex()

