class Base:
    def getdata(self):
        self.num=eval(input("Enter any number :"))


class Derive(Base):
    def calCube(self):
        self.cube=self.num**3
        print("Cube of a number is : ",self.cube)



d=Derive()
d.getdata()
d.calCube()
