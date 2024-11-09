# from venv import create

from TRANSACTIONS.module import searchAccount, createAccount, showAccount, depositMoney, withdrawMoney

while True:
    print("1. Add Account")
    print("2. Show Account")
    print("3. Deposit Money")
    print("4. Withdraw Amount")
    print("5. Statement")
    print("6. Exit")

    choice = int(input("select option : "))

    if choice==1:
        if createAccount():
            print("Successfully created account")
        else:
            print("Something went wrong. try again")

    elif choice==2:
        info= showAccount()
        
        print("%10s %20s %20s" % ("Acc No", "Account Name", "Opening Balance"))
        print("%10d %20s %20.2f" % (info[0], info[1], info[2]))

    elif choice==3:
        info = depositMoney()
        print("Amount Rs.", info[0], " credited to account number ", info[1])

    elif choice ==4:
        info = withdrawMoney()
        print("Amount Rs.", info[0], " debited from account number ", info[1])

    elif choice==5:
        pass

    elif choice==6:
        break
