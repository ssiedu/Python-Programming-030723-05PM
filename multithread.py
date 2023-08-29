import threading
import time
def square(n):
    for num in n:
        time.sleep(0.7)
        print("square :",num*num)

def cube(n):
    for num in n:
        time.sleep(0.7)
        print("Cube :",num*num*num)

l1=[2,3,4,5]
t1=threading.Thread(target=square,args=(l1,))
t2=threading.Thread(target=cube,args=(l1,))
t1.start()
time.sleep(0.5)
t2.start()
t1.join()
t2.join()
print("Finished Process")
