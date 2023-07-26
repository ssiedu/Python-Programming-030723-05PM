num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
num3=int(input("Enter Third Number :"))
if num1>num2 and num1>num3:
    print(num1," is largest number ")
elif num2>num3:
    print(num2," is largest number ")
else:
    print(num3," is largest number ")
