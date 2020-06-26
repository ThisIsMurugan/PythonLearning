list = ['Murugan','Sowmya','Tamil','Test1','Test2']
print(type(list))
print(list[0]) #First in the List
print(list[-1]) #Last in the List
print(list[0:3])
print(list[-3:-1])

for temp in list:
    print(temp)
if "Murugan1" in list:
    print('found')
else:
    print('Not found')