class Base:
    def __init__(self):
        print("This is base class Function")


class Derive(Base):
    def __init__(self):
        super().__init__()
        #Base.__init__(self)
        print("This is derive class function")


D=Derive()
#D.getdata()
