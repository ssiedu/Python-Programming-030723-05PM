p=int(input("Enter principle amount :"))
r=int(input("Enter rate of interest :"))
t=int(input("Enter time in year :"))
si=(p*r*t)/100
total=p+si
print("Simple interest :",si)
print("Total amount :",total)
