class Base:
    def __init__(self):
        self.num1=eval(input("Enter First Number :"))
        self.num2=eval(input("Enter Second Number :"))

class Child1(Base):
    def calAdd(self):
        self.add=self.num1+self.num2
        print(" sum is : ",self.add)

class Child2(Base):
    def calMod(self):
        self.mod=self.num1%self.num2
        print("Modulus :",self.mod)

class Child3(Base):
    def calFD(self):
        self.fd=self.num1//self.num2
        print("Floor Division :",self.fd)


C1=Child1()
C1.calAdd()
C2=Child2()
C2.calMod()
C3=Child3()
C3.calFD()




        
