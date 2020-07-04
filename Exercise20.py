def list1(l):
    list2=[]
    for i in l:
        if type(i)==int or type(i)==float:
            i=str(i)
            list2.append(i)
    print("your new list is: ",list2)

list3=['a','Pankaj',[1.5,'ja',5],25,5.5]
list1(list3)
        
