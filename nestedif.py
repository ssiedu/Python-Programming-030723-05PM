num1=int(input("Enter First number :"))
num2=int(input("Enter Second Number :"))
if num1!=num2:
    print(num1," is not equal to ",num2)
    if num1>num2:
        print(num1," is greater number")
    else:
        print(num2," is greater number")
else:
    print("Both are Equal")
