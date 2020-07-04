class Dev1:
    def __init__(self):
        self.a=1
        self.b=2

    def showdata(self):
        print(self.a,self.b)
class Dev2(Dev1):
    def __init__(self):
        self.c=11
        self.d=22
        super().__init__()
    def showdata(self):
        print(self.c,self.d)
class Dev3(Dev2):
    def __init__(self):
        self.e=11
        self.f=22
        super().__init__()
    def showdata(self):
        print(self.e,self.f)
ob1=Dev1()
ob2=Dev2()
ob3=Dev3()
print(ob1.__dict__)
print(ob2.__dict__)
print(ob3.__dict__)
Dev1.showdata(ob3)
print(ob3.a)