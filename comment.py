#This is single line comment
print("Single line comment")
'''This is
multiline
comment'''
print("Multiline comment")


#docstring comment

def demo():
    """This isdocstring comment"""
    print("This is demo function")


demo()
print(demo.__doc__)
