#Tuple
#Tuple are immutable : it means we can't done (insert,append,extend,pop,remove methods on tuple)
#in tuple we can use only (count,index,len,slicing)
example=(1,2,3,"pankaj","agrawal",2.0,3.5)
print(example)
example2=(1,)
print("one element tuple",example2)
for i in example:
    print("tuple with for loop",i)
example3='pankaj','kumar','agrawal'
print("tuple without paranthesis",example3)

#Tuple unpacking : number of element in tuple equal to packing element
#here no. of element in tuple(e.g. example4 '4' element present and in next line we see number of unpacking element are also '4'(ex1,ex2,ex3,ex4)
example4=('Lord Krishna','Pankaj','Shraddha','Tiger')
ex1,ex2,ex3,ex4=(example4)
print("Tuple unpacking",ex1)

#Tuple creation by (tuple)
example5=tuple(range(1,11))
print("tuple by tuple method",example5)

#Tuple in string
example6=str((1,2,3,4))
print('Tuple in string',example6)
print("typle of example6 is",type(example6))

