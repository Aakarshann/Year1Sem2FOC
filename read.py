from operation import *
def read():
    file=open('storeItems.txt','r')
    itemDictionary={}
    itemID=1
    for line in file:
     line=line.replace('\n','')
     itemDictionary[itemID]=line.split(',')
     itemID=itemID+1
    file.close()
    return itemDictionary

