class Addition:
    def getdata(self):
        self.n1=eval(input("Enter First Number :"))
        self.n2=eval(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.n1+self.n2
    def display(self):
        print("Addition :",self.add)


A=Addition()
A.getdata()
A.calAdd()
A.display()
