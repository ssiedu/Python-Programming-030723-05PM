list1=[]
file=open("Myfile5.txt","w")
for i in range(5):
    name=input("Enter Student Name :")
    list1.append(name+"\n")

file.writelines(list1)
file.close()
