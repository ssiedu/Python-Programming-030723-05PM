class SI:
    def getdata(self):
        self.__p=eval(input("Enter principle amount :"))
        self.__r=eval(input("Enter rate of interest :"))
        self.__t=eval(input("Enter time in year :"))
    def calSI(self):
        self.si=(self.__p*self.__r*self.__t)/100
        self.total=self.__p+self.si
    def display(self):
        print("Simple Interest :",self.si)
        print("Total Amount :",self.total)


obj=SI()
obj.getdata()
obj.calSI()
obj.display()
#print("principle amount :",obj.__p)
