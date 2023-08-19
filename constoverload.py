class Addition:
    def __init__(self):
        self.num1=100
        self.num2=200
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition :",self.add)


add=Addition()
add.calAdd()
