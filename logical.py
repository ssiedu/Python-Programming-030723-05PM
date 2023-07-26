a=int(input("Enter First Number :"))#10
b=int(input("Enter Second Number :"))#20
c=int(input("Enter third Number :"))#10

print("And :",((a>b) and (b==c)))#False
print("Or  :", ((a!=b) or not(c)))#True
print(" And not :",((a>c) and not(b==a)))#False
print("Or not :",not((a!=b) or (c>a)))#False
print("and not or :",(not(a==c) and ((a>c) or (b>c))))#False
print(" and or :",(((b>=c) and (a!=b)) or (a==c)))#True


