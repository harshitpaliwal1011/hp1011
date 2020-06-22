def deposit(an,amt):
    for item in actInfo:
        item = list(item)
        if item[0] == an:
            item[2] +=amt
            print("Your account balance is %0.2f\n Thank you for using this ATM !" %item[2])

def withdraw(an,amt):
    for item in actInfo:
        item = list(item)
        if item[0] == an:
            if item[2] <= amt:
                print("Insufficient Balance")
            else:
                item[2]-=amt
            print("Your account balance is %0.2f\n Thank you for using this ATM !" %item[2])

def acop():
    an = int(input("Enter your AC no:"))
    for item in actInfo:
        if item[0] == an:
            print("Welcome %s"%item[1])
    amt = int(input("Enter deposit/withdraw amount:"))
    b=int(input("Press 1 for Deposit\nPress 2 for Withdrawal\n"))
    if b == 1:
        deposit(an,amt)
    elif b == 2:
        withdraw(an,amt)
    else:
        print("Incorrect Input!!")

print("Creating 2 new accounts.")
actInfo = []
for i in range(2):
    an = int(input("Enter AC no :"))
    ahn = input("Enter AC Holder's name :")
    ab = float(input("Enter Ac balance :"))
    tup = (an,ahn,ab)
    actInfo.append(tup)
else:
    print(actInfo)

a=input("Do you wish to perform an account operation(y/n): ")
if a == "y" or a == "Y":
    acop()
else:
    print("Thank you for using this ATM !!")
