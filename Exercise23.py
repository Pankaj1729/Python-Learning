def position(w,l):
    for i in range(len(l)):
        if l[i]==w:
            print("Position of",l[i],"is",i+1) 
    else:
        print("Element not found")

l=['Pankaj','Shraddha','Priti','Krishna']
s=input("Enter element for search ")
position(s,l)
    
