def number_of_list(l1):
    j=0
    for i in l1:
        if type(i)==type(l1):
                j+=1
    return j
list1=[]
n=int(input("enter number of element you want in list :"))
for i in range(n):
    list1.append(int(input()))
print("list1 is :",list1)
print("number of list in list1 are :",number_of_list(list1))
