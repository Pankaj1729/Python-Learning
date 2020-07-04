#Dictionary -: unoredered collection of data with key value pair
dict1={'Name':'Panakj','age':18,1:1729}
print(dict1)
print(len(dict1))

#dictionary by dict method
example1=dict(name='Pankaj Kumar',age=18)
print('dictionary with dict method',example1)

#No indexing present in dictionary
#here we use key
print("data excess by key not by index :" ,example1['name'])

#in dictionary (string,list)
example2={
    'name':'Pankaj Kumar Agrawal', 'age':18,
    'fav_movie':['Marvel Universe','ABCD2']
    ,1:1729
    }
print(example2)

#to print all key value
for i in example2:
    print(type(i))
    print("keys of example2", i)
#by key value
for i in example1.keys():
    print("key of example1", i)
    print(type(i))

#To read value from dictonary
for i in example2.values():
    print(i)

#to print item : it rerturn key-value pair  
for i in example2.items():
    print(i)

#update method:
example3={'a':"all",'22':'a22'}
example2.update(example3)
print(example2)

#pop method : it return value corresponding to that key
print(example3.pop('22'))
print(example3)

#popitems method : it return key-value pair
print(example2.popitem())

