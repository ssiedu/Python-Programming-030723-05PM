num=int(input("Enter any number :"))
if num==0:
    print("Zero")
elif num>0:
    print("Positive Number")
    if num%2==0:
        print("Even Number")
    else:
        print("Odd number")
else:
    print("Negative Number")
    if num%2==0:
        print("Even Number")
    else:
        print("Odd number")
        
