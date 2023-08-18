class EvenOdd:
    def getdata(self):
        self.num=int(input("Enter any number :"))
    def checkNum(self):
        if self.num%2==0:
            print("Even Number ")
        else:
            print("Odd Number ")


eo=EvenOdd()
eo.getdata()
eo.checkNum()
