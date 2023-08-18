class Loop:
    def getNum(self):
        self.num=int(input("Enter any number :"))
    def SeriesPrint(self):
        i=self.num
        sum=0
        while i>0:
            print(i,end=" ")
            sum=sum+i
            i=i-1
        print("\nSum is :",sum)


L=Loop()
L.getNum()
L.SeriesPrint()
