class Area:
    def __init__(self):
        self.l=eval(input("Enter Length :"))
        self.b=eval(input("Enter breadth :"))
    def calArea(self):
        self.area=self.l*self.b
        print("Area of rectangle :",self.area)
