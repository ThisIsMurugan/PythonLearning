listId = [10,20,30]
listName = ["Murugan","Sowmya","Tamil"]
listCountry = ["IND","USD","UK"]
#zip the data
listZip = zip(listId,listName,listCountry)
listZip = list(listZip)
print("Zipped data")
for dataId,dataName,dataCountry in listZip:
    print(dataId,dataName,dataCountry)


#unzip the data
print("Unzipped data - back to list")
w1,w2,w3 = zip(*listZip)
print(w1,w2,w3)
