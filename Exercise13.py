def square_of_list(l):
    list1=[]
    for i in  l:    
        list1.append(i*i)
    print(list1)

n=int(input("enter number element you want to get their square :"))
lst=list(range(1,n+1))
square_of_list(lst)
