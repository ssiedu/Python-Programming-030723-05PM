ch=input("Enter any value :")
if ch>='a' and ch<='z':
    print("Lower case letter")
elif ch>='A' and ch<='Z':
    print("Upper case letter")
elif ch>='0' and ch<='9':
    print("Digit")
else:
    print("Special Symbol")
