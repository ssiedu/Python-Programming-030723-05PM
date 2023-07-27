num=int(input("Enter any number :"))
if num%2==0:
    print("Number is divisible by 2")
    if num%3==0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisible by 3")
else:
    print("Number is not divisible by 2")
    if num%5==0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
