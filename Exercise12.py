def pallindrom(name1,name2):
    if name1==name2:
        return True
    else:
        return False

a=input("enter any name :")
b=a[::-1]
print(pallindrom(a,b))

        
