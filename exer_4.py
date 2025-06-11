myDict = {
    'Name'  : 'Danny',
    'Age'   : 100
}

print(myDict)
print(myDict['Name'])

myDict['Session'] = 'Evening'

myDict['Session'] = 'Weekend'

myDict['Module'] = 'Python'

del myDict['Session']

for key, value in myDict.items():
    print(f"{key} : {value}")