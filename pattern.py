#n=int(input("enter a number "))
'''
for i in range(n):
    for j in range(n-i-1):
        print(end=' ')
    for k in range(i+1):
        print(end='*')
    print() for next line
   output :
    *
   **
  ***
 ****
***** 
'''
'''
for i in range (n):
    for j in range(i+1):
        print(end="*")
    for k in range(2*(n-i-1)):
        print(end=' ')
    for m in range(i+1):
        print(end='*')
    print()
output:
*        *
**      **
***    ***
****  ****
**********
'''
x="pnamta"
y='akjitl'
for i in range(len(x)):
    if i==3:
        print(end=' ')
    print(x[i] + y[i],end='')
