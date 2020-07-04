class SeprateValue:
    list1=[]
    list2=[]
    def __init__(self):
        pass
    def addInteger(self):
        n=int(input("Enter how many Integer value store in list: "))
        for i in range(n):
            list1.append(int(input())
        return self.list1

while True:
    print("choose type of value you want to store in your list! \nChoises are:")
    print("1.Inte3ger data\n2.Float value\n3.String value\n0.Nothig to fiil or Exit")
    choice=int(input("Enter Your choice "))
    if choice==1:
        obj=SeprateValue()
        a=obj.addInteger()
        print(a)
    if choice==0:
        break

