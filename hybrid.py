class Base:
    def __init__(self):
        self.l=eval(input("Enter Length of rectangle :"))
        self.b=eval(input("Enter breadth of rectangle :"))

class Parent1(Base):
    def calArea(self):
        self.rarea=self.l*self.b

class Parent2:
    def getdata(self):
        self.r=eval(input("Enter radius of circle :"))
    def calCArea(self):
        self.carea=3.14*self.r*self.r
        
class Child(Parent1,Parent2):
    def display(self):
        print("Area of rectangle :",self.rarea)
        print("Area of circle    :%.2f"%self.carea)


C=Child()
C.calArea()
C.getdata()
C.calCArea()
C.display()





        
