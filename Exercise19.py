dict1={}
def dictionary_of_cube(d):
    for i in range(1,d+1):
        dict1[i]=i*i*i
    return dict1

n=int(input("enter number of element :" ))
print("Dictionary is :",dictionary_of_cube(n))
