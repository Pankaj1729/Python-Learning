def num_pow(n,*args):
    dict1={i:i**n for i in args}
    print(dict1)
n=int(input("Enter number of element "))
tuple1=[]
for i in range(n):
    tuple1.append(int(input("enter element in list ")))
n1=int(input("Enter power "))

num_pow(n1,*tuple1)#tuple unpacking



#(*args) work as tuple
