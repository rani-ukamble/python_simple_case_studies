# from re import search

def searchAccount():
    an = int(input("Enter account number to see details: "))
    if an == accno:
        return True
    else:
        return False

def createAccount():
    global accno
    global accname
    global opening_balance

    accno = int(input("Enter account number: "))
    accname = input("Enter account holder name: ")
    opening_balance = float(input("Enter opening balance: "))

    return True

def showAccount():
    if searchAccount():
        return accno, accname, opening_balance
    else:
        # print("Invalid account")
        return False

def depositMoney():
    global opening_balance  # Declare it as global
    if searchAccount():
        damt = float(input("Enter amount: "))
        opening_balance += damt
        # print("Amount Rs.", damt, " credited to account number ", accno)
        return damt, accno
    else:
        # print("Invalid account")
        return False

def withdrawMoney():
    global opening_balance  # Declare it as global
    if searchAccount():
        wamt = float(input("Enter amount: "))

        if wamt <= opening_balance:
            opening_balance -= wamt
            # print("Amount Rs.", wamt, " debited from account number ", accno)
            return wamt, accno
        else:
            # print("Less balance.")
            return False
    else:
        # print("Invalid account")
        return False
   