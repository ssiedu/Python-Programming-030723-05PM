from multipledispatch import dispatch

@dispatch(int,int)
def Product(fnum,snum):
    result=fnum*snum
    print("Product of two int value :",result)

@dispatch(int,float)
def Product(fnum,snum):
    result=fnum*snum
    print("Product of two diff value :",result)

@dispatch(int,int,int)
def Product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("Product of three int value :",result)

@dispatch(float,float)
def Product(fnum,snum):
    result=fnum*snum
    print("Product of two float value :",result)

Product(10,2)
Product(2.1,3.4)
Product(10,2.3)
Product(10,20)
Product(2,3,4)




    
