def ref(data):
    #data[1]="apple"
    data.append("ssi")


list1=[11,22,33,44,55]
print("Before function call")
print(list1)
ref(list1)
print("After function call ")
print(list1)
