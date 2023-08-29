try:
    a=10
    b='0'
    c=a/b
    print("value of c :",c)
except ZeroDivisionError:
    print("Zero Division Error")

except:
    print("Type Mismatch")
