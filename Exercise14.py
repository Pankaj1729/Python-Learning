list1=[]
n=int(input("enter no. of element in list :"))
for i in range(n):
    list1.append(int(input()))
print("list1 is :",list1)
list2=[]
for i in range(n):
    list2.append(list1.pop())
print("list2 is :",list2)
