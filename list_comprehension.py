list1=[]
n=int(input("Enter number of element: "))
for i in range(n):
    list1.append(input())
print("original list: ",list1)
list2=[i[::-1] for i in list1]
print("inverted list: ",list2)
