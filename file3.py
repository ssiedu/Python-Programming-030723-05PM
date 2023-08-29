file=open("Myfile3.txt","w")
n=int(input("How many Records do you want to Enter :"))
for i in range(n):
    name=input("Enter employee Name :")
    id=int(input("Enter Employee Id :"))
    sal=eval(input("Enter Employee Salary :"))
    data= name+"\t"+str(id)+"\t"+str(sal)+"\n"
    file.write(data)
file.close()
