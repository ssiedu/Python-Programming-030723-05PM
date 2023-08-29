import pickle
file=open("Myfile7","wb")
list1=[11,22,33,44,55]
pickle.dump(list1,file)
file.close()
file=open("Myfile7","rb")
data=pickle.load(file)
print(data)
file.close()
