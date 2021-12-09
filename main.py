
import sys
import os
from generate import generate
import pandas as pd
import csv
x=generate()
x.loadlexicon()


print(x.lexicon)
print("welcome")

df = pd.DataFrame.from_dict(x.lexicon, orient="index")

df.to_csv('GFG.csv')
a=pd.read_csv('lexicon.csv')
print(a)
