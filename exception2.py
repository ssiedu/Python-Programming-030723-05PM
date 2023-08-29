try:
    print("Try Block")
    n1=int(input("Enter First number :"))
    n2=int(input("Enter Second Number :"))
    res=n1/n2

except:
    print("Except Block")
    print("Some Error Occured")

else:
    print("Else Block")
    print("Result is :",res)

finally:
    print("Finally Block")
    print("Successfully Executed")
