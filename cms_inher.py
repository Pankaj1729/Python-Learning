class Employee:
    emplist = []

    @staticmethod
    def getypeyid(id):
        for e in Employee.emplist:
            if e.id==id:
                return e.type

    @staticmethod
    def cheakid(id):
        for e in Employee.emplist:
            if e.id==id:
                return True


    @staticmethod
    def getempbyid(id):
        for e in Employee.emplist:
            if e.id==id:
                if e.type=="Director":
                    return Director()
                elif e.type=="Manager":
                    return Manager()
                elif e.type=="Tester":
                    return Tester()


    def __init__(self):
        self.id = 0
        self.name = None
        self.type = None

    def __str__(self):
        return "ID:"+str(self.id)+  "  "  + "Name:"+str(self.name)+ "    "  +   "Type:"+self.type

    def add(self):
        Employee.emplist.append(self)

    def search(self,id):
        for e in Employee.emplist:
            if e.id==id:
                self.id=e.id
                self.name = e.name
                self.type = e.type


    def modify(self,id):
        for e in Employee.emplist:
            if e.id==id:
                if self.name == None:
                    e.name=e.name
                else:
                    e.name=self.name
                if self.type == None:
                    e.type=e.type
                else:
                    e.type=self.type

    def delete(self,id):
        for e in Employee.emplist:
            if e.id==id:
                i=Employee.emplist.index(e)
                Employee.emplist.pop(i)

class Manager(Employee):

    def __init__(self):
        self.mgrspecial = None
        self.incentive = None
        super().__init__()

    def __str__(self):
        return      super(Manager, self).__str__()+ "  "    +"mgrspecial:" + str(self.mgrspecial) +"  " +"incentive:" + str(self.incentive)

    def add(self):
        super().add()

    def search(self,id):
        for e in Employee.emplist:
            if e.id==id:
                self.mgrspecial=e.mgrspecial
                self.incentive = e.incentive
                super().search(id)

    def modify(self,id):
        for e in Employee.emplist:
            if e.id==id:
                if self.mgrspecial==None:
                    e.mgrspecial=e.mgrspecial
                else:
                    e.mgrspecial=self.mgrspecial
                if self.incentive==None:
                    e.incentive=e.incentive
                else:
                    e.incentive=self.incentive
        super().modify(id)

    def delete(self,id):
        super().delete(id)


class Director(Employee):
    def __init__(self):
        self.share = None
        self.direspecial = None
        super().__init__()

    def __str__(self):
        return      super().__str__() + "  "   + "Direspecial:" + str(self.direspecial)+ "  " + "Share:" + str(self.share)

    def add(self):
        super().add()

    def search(self,id):
        for e in Employee.emplist:
            if e.id==id:
                self.share=e.share
                self.direspecial = e.direspecial
                super().search(id)

    def modify(self,id):
        for e in Employee.emplist:
            if e.id==id:
                if self.share == None:
                    e.share=self.share
                else:
                    e.share=self.share
                if self.direspecial==None:
                    e.direspecial=self.direspecial
                else:
                    e.direspecial=self.direspecial
        super().modify(id)

    def delete(self,id):
        super().delete(id)

class Tester(Employee):
    def __init__(self):
        self.tspecial = None
        self.salary = None
        super().__init__()
    def __str__(self):
        return      super().__str__()+"  "+"salary:" + str(self.salary)+"  "+"tspecial:" + str(self.tspecial)

    def add(self):
        super().add()

    def search(self,id):
        for e in Employee.emplist:
            if e.id==id:
                self.tspecial=e.tspecial
                self.salary = e.salary
                super().search(id)

    def modify(self,id):
        for e in Employee.emplist:
            if e.id==id:
                if self.salary==None:
                    e.salary=e.salary
                else:
                    e.salary=self.salary
                if self.tspecial==None:
                    e.tspecial=e.tspecial
                else:
                    e.tspecial=self.tspecial
        super().modify(id)
    def delete(self,id):
        super().delete(id)


while True:
    print("1.Add Emp!")
    print("2.Search Emp!")
    print("3.Modify Emp!")
    print("4.Delete Emp")
    print("5.Exit!")
    print('-------------------')
    ch=int(input("Enter your choice:"))
    print('--------------------')

    if ch==1:
        print("1.add Director!")
        print("2.add Manager!")
        print("3.add Tester!")
        print('-------------------')
        ch1 = int(input("Enter your choice:"))
        print('--------------------')
        
        if ch1==1:
            while True:
                id=int(input("Enter id:"))
                if Employee.cheakid(id):
                    print("Does not exist:")
                else:
                    break
            obdir = Director()
            obdir.id = id
            obdir.name = input("Enter name:")
            obdir.type = "Director"
            obdir.share = input("Enter share:")
            obdir.direspecial = input("Enter dirspecial")
            obdir.add()
            print("Added successfully!")
            print(obdir.__dict__)
        elif ch1 == 2:
            while True:
                id=int(input("Enter id:"))
                if Employee.cheakid(id):
                    print("Does not exist:")
                else:
                    break

            obmgr = Manager()
            obmgr.id = id
            obmgr.name = input("Enter name:")
            obmgr.type = "Manager"
            obmgr.incentive = input("Enter incentive:")
            obmgr.mgrspecial = input("Enter mgrspecial")
            obmgr.add()
            
        elif ch1==3:
            while True:
                id = int(input("Enter id:"))
                if Employee.cheakid(id):
                    print("Does not exist:")
                else:
                    break
            obtester = Tester()
            obtester.id = id
            obtester.name = input("Enter name:")
            obtester.type = "Tester"
            obtester.tspecial = input("Enter tspecial:")
            obtester.salary = input("Enter salary:")
            obtester.add()
                #print(obtester.__dict__)

    elif ch==2:
        if len(Employee.emplist)==0:
            print("No data!")
            print('---------------------')
        else:
            id=int(input("Enter id to search data:"))
            obj=Employee.getempbyid(id)
            obj.search(id)
            print(obj)
    elif ch == 3:
        if len(Employee.emplist) == 0:
            print("NO DATA TO MODIFY!")
            print("---------------------!")
        else:
            id=int(input("Enter id to modify:"))
            while True:
                obj = Employee.getempbyid(id)
                if Employee.getypeyid(id) == "Director":
                    print("This emp is Director")
                    print("you can change:\n1.name\n3.direspecial\n4.share")
                    print("---------------------------------")
                    print("Enter 'no' for not modification:")
                    print('----------------------------------')
                    chc = input("Enter parameter to modify:")
                    print("--------------------------------")
                    if chc == "direspecial":
                        obj.direspecial = input("Enter new direspecial:")
                        obj.modify(id)
                    elif chc == "share":
                        obj.share = input("Enter  new share:")
                        obj.modify(id)
                    elif chc == "name":
                        obj.name = input("Enter  new name:")
                        obj.modify(id)
                    elif chc == "type":
                        obj.type = input("Enter  new share:")
                        obj.modify(id)
                    elif chc == 'no':
                        break
                elif Employee.getypeyid(id)=="Manager":
                    print("This emp is Manager!")
                    print("you can change:\n1.name\n3.mgrspecial\n4.incentive")
                    print("---------------------------------")
                    print("Enter 'no' for not modification:")
                    print('----------------------------------')
                    chc = input("Enter parameter to modify:")
                    print("--------------------------------")
                    if chc == "mgrspecial":
                        obj.mgrspecial = input("Enter new mgrspecial:")
                        obj.modify(id)
                    elif chc == "incentive":
                        obj.incentive = input("Enter  new incentive:")
                        obj.modify(id)
                    elif chc == "name":
                        obj.name = input("Enter  new name:")
                        obj.modify(id)
                    elif chc == "type":
                        obj.type = input("Enter  new type:")
                        obj.modify(id)
                    elif chc == 'no':
                        break

                elif Employee.getypeyid(id) == "Tester":
                    print("This emp is Tester!")
                    print("you can change:\n1.name\n3.tspecial\n4.salary")
                    print("---------------------------------")
                    print("Enter 'no' for not modification:")
                    print('----------------------------------')
                    chc = input("Enter parameter to modify:")
                    print("--------------------------------")
                    if chc == "tspecial":
                        obj.tspecial = input("Enter new tspecial:")
                        obj.modify(id)
                    elif chc == "salary":
                        obj.salary = input("Enter  new salary:")
                        obj.modify(id)
                    elif chc == "name":
                        obj.name = input("Enter  new name:")
                        obj.modify(id)
                    elif chc == "type":
                        obj.type = input("Enter  new type:")
                        obj.modify(id)
                    elif chc == 'no':
                        break

    elif ch==4:
        if len(Employee.emplist)==0:
            print("NO DATA TO DELETE!")
        else:
            id=int(input("Enter id to delete:"))
            obj=Employee.getempbyid(id)
            obj.delete(id)
            print("Deleted successfully!")
            print("------------------------")
    elif ch==5:
        print("Thank You!")
        break