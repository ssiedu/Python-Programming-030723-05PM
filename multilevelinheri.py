class GrandParent:
    def getdata(self):
        self.p=eval(input("Enter principle amount :"))
        self.r=eval(input("Enter rate of interest :"))
        self.t=eval(input("Enter time in year :"))


class Parent(GrandParent):
    def calSI(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.p+self.si


class Child(Parent):
    def display(self):
        print("Simple Interest : ",self.si)
        print("Total amount : ", self.total)


C=Child()
C.getdata()
C.calSI()
C.display()





