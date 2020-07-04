##def add(*p):
##    sum=0
##    for i in p:
##        sum+=i
##    return sum
##
##n=int(input("Enter number of value "))
##v=[int(input()) for i in range(n)]
##print("sum of numbers is:",add(*v))
if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    largest=int(arr[0])
    largest2=0
    for item in arr[1:]:
        item=int(item)
        print(item,largest,largest2)      
        if item > largest:
            item=int(item)
            largest2 = largest 
            largest = item
            print('True')
        elif item==largest:
            print('True1')
            continue  
        elif largest2 == 0 or largest2< item or largest2== item :
            largest2 = item
            print('True') 
    print(largest2)
    print(largest)
    
