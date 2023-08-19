class Addition:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition :",self.add)

x=eval(input("Enter first Number :"))
y=eval(input("Enter Second Number :"))
add=Addition(x,y)
add.calAdd()
