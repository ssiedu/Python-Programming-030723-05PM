class Addition:
    def getdata(self):
        self.num1=eval(input("Enter first Number :"))
        self.num2=eval(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition :",self.add)


add=Addition()
add.getdata()
add.calAdd()
