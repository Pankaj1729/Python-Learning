n=input("enter a number for sum of their digit : ")
k=n
j=len(n)
sum=0
n=int(n)
while j!=0:
    t=n%10
    sum+=t
    n=n//10
    j-=1

print(f"sum of digit of value : {k} is {sum}") 
      
