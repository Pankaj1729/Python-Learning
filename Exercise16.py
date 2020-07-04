import random
list1=[]
list2=[]
list3=[]
def even_odd_list(list):
    for i in list:
        if i%2==0:
            list1.append(i)
        else:
            list2.append(i)
    list3.append(list1)
    list3.append(list2)
    return list3 

#n=int(input("enter how number want to insert in list :"))
your_list=[]
#for i in range(n):
for i in range(random.randint(1,100)):
    #your_list.append(int(input())
    your_list.append(i)
print("your entered list is :",your_list,'\n','In which even,odd are :' ,even_odd_list(your_list))
    

