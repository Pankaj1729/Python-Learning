def fact(n):
    facto=1
    for i in range(1,n+1):
            facto = facto*i
            i+=1
    return facto
n=int(input("enter a number :"))
print(fact(n))
