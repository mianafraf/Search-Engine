from os import listdir, remove
from nltk.stem import PorterStemmer
from generate import generate
from nltk.corpus import stopwords
import numpy as np

v = generate()
search = input("Search:   ")
search = search.split()
print(search)

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

x = 0
stemmedSearch = []
while x < len(search):
    if len(search[x]) <= 1:
        pass
    else:
        if search[x] in stop_words:
            pass
        else:
            if search[x].isalpha():
                search[x] = ps.stem(search[x])
                if (search[x] in stemmedSearch) != 1:
                    stemmedSearch.append(search[x])
    x += 1

print(stemmedSearch)

v.loadlexicon()
v.loadinvindex()
v.loaddocids()

index = 0
# articleList = {}
# for x in stemmedSearch:
#     try:
#         wordID = int(v.lexicon[x])
#         if index == 0:
#             articleList = [v.invindex[wordID]]
#         else:
#             articleList.append(v.invindex[wordID])
#         index += 1
#     except KeyError:
#         pass

articleList = []
for x in stemmedSearch:
    try:
        wordID = int(v.lexicon[x])
        if index == 0:
            articleList = [v.invindex[wordID]]
        else:
            articleList.append(v.invindex[wordID])
        index += 1
    except KeyError:
        pass

print(articleList)

index = 0
intersectedList = []
unintersectedList = []
# for x in articleList:
#     if index == 0:
#         intersectedList = x
#         index += 1
#     else:
#         intersectedList = set.intersection(set(intersectedList), set(x))

def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

for x in articleList:
    if index == 0:
        intersectedList = x
        index += 1
    else:
        intersectedList = intersection(intersectedList, x)
        
print(intersectedList)

# for item in intersectedList:
#     print(v.doc[item][0])
#     print(v.doc[item][1])

for x in articleList:
    unintersectedList.append(Diff(x, intersectedList))

index = 0
odUnintersectedList = []
for x in unintersectedList:
    for item in x:
        odUnintersectedList.append(item)

print(odUnintersectedList)

#zealand counterpart winston peter
finalList = intersectedList + odUnintersectedList

print(finalList)

for x in finalList:
    print(v.doc[x][0])
    print(v.doc[x][1])