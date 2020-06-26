from sklearn.linear_model import LinearRegression
fileData = open('SampleFile.txt', 'r')
weight = []
noOfPeople = []
for data in fileData:
    _noOfPeople,_weight = data.split(',')
    noOfPeople.append([int(_noOfPeople)])
    weight.append(float(_weight))

linearObject = LinearRegression()
#Y = MX + C
linearObject.fit(noOfPeople,weight)
print(linearObject.predict([[5]]))