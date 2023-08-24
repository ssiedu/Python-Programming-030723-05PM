import random
while True:
    uc=input('''Game Start...
1.Yes('y'||'Y')
2.Exit('n'||'N')
''')
    if uc.lower()=='y': #or uc=='Y':
        com_input=random.randint(1,3)
        user_input=int(input("Enter any number :"))
        if com_input>user_input:
            print("Computer value :",com_input)
            print("Your guess number is smallest Number")
        elif user_input>com_input:
            print("Computer value :",com_input)
            print("Your Guess number is Largest number")
        else:
            print("Computer value :",com_input)
            print("Both are Equal")
    else:
        break;
