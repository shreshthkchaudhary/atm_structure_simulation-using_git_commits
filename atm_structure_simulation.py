def check_balance(balance):
    print(f"\nYour Current Balance is Rs{balance}\n")

def deposit_amount(balance):
    deposit=float(input("Enter amount to Deposit :Rs"))
    if deposit>=1:
        balance+=deposit
        print(f"Rs{deposit} deposited successfully.\n")
        print(f"Your current balance is Rs{balance}\n")
    else:
        print("Invalid entered Amount")
        deposit_amount(balance)
    return balance

def withdrawal_amount(balance):
    withdrawal=float(input("Enter amount to withdraw :Rs"))
    if withdrawal==0:
        print(f"Invaled Amount Enter Amount More then Rs0")
        withdrawal_amount(balance)
    elif withdrawal<=balance:
        balance-=withdrawal
        print(f"Rs{withdrawal} withdrawn successfully.\n")
        print(f"Your current balance is Rs{balance}\n")

    else:
        print("insufficient balance")
        withdrawal_amount(balance)

    return balance

def exit_menu():
    print("\nThank you for using ATM")

def sub_menu():
    print("To go to Main Menu give input 1")
    print("To Exit give input 2\n")
    sub_option=int(input("Choice option: Enter your choice (1-2):"))
    while 1!=sub_option!=2:
        print("Invalid Option Choice between (1-2)")
        sub_option=int(input("Choice option: Enter your choice (1-2):"))
    if sub_option==1:
        main_menu()
    else:
        exit_menu()

def main_menu():
    balance=1000.00
    print("\nATM Menu:")
    print("To Check Balance give input 1")
    print("To Deposit Amount give input 2")
    print("To do Withdrawal give input 3")
    print("To Exit give input 4")
    option=int(input("\nChoice option: Enter your choice (1-4):"))
    if option==1:
        check_balance(balance)
        sub_menu()

    elif option==2:
        deposit_amount(balance)
        sub_menu()

    elif option==3:
        withdrawal_amount(balance)
        sub_menu()

    elif option==4:
        exit_menu()

    else:
        print("Invalid Option Choice between (1-4)")
        main_menu()

main_menu()
