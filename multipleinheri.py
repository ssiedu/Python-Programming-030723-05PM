class Base1:
    def __init__(self):
        self.num1=eval(input("Enter First Number :"))

class Base2:
    def getNum2(self):
        self.num2=eval(input("Enter Second Number :"))

class Base3:
    def getNum3(self):
        self.num3=eval(input("Enter Third Number :"))

class child(Base1,Base2,Base3):
    def product(self):
        self.pro=self.num1*self.num2*self.num3
    def display(self):
        print("Product of numbers :",self.pro)


C=child()
#C.getNum1()
C.getNum2()
C.getNum3()
C.product()
C.display()


