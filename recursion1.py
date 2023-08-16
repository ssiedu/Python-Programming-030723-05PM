def number(n):
    if(n==1):
        return 1;
    else:
        return n*number(n-1)


print(number(5))
