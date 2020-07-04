def common_element_in_list(l1,l2):
    list3=[]
    for i in l1:
        for j in l2:
            if i==j:
                list3.append(i)
    return list3
list1=[]
list2=[]
m=int(input("enter number of element you want in list1 :"))
print("enter element in list1")
for i in range(m):
    list1.append(int(input()))
print("list1 is :",list1)
n=int(input("enter number of element you want in list2 :"))
print("enter element in list2")
for i in range(n):
    list2.append(int(input()))
print("list2 is :",list2)
print("common element in list1 and list2 are :",common_element_in_list(list1,list2))
