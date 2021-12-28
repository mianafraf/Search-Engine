from generate import generate
v = generate()
v.loadfindex()
v.loadinvindex()

# insert any value into wordid to get it's number of occurrences in the documents that contain it
wordid = 0
for doclist in v.invindex[wordid]:
    for indexlist in v.findex[doclist]:
        if indexlist[0] == wordid:
            print (len(indexlist[1:]))
