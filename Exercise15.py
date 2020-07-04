reverse_list=[]
def reverse_list_element(list):
    for i in list:
        for j in range(len(i)):
            q=i[::-1]
        reverse_list.append(q)
    return reverse_list
original_list=[]
n=int(input("enter number of element want in list :"))
for i in range(n):
    original_list.append(input())
print("original list :",original_list)
print("reversed list :",reverse_list_element(original_list))
            
