while True:
    uc=input('''Do you Want to continue -
1.Yes
2.Exit
''')
    if uc.lower()=='y':
        print('''Please Select Any One :-
1.Addition
2.Subtraction
3.Multiplication
4.Division
''')

        fnum=int(input("Enter First Number :"))
        ch=input("Enter your choice :")
        snum=int(input("Enter Second Number :"))

        match ch:
            case '+':
                print("{} + {} = {}".format(fnum,snum,fnum+snum))
            case '-':
                print("{} - {} = {}".format(fnum,snum,fnum-snum))
            case '*':
                print("{} * {} = {}".format(fnum,snum,fnum*snum))
            case '/':
                print("{} / {} = {}".format(fnum,snum,fnum/snum))
            case _:
                print("Please Enter valid choice")
    else:
        break;
