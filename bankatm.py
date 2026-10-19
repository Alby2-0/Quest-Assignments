balance=10000

while True:
    print("====BANK ATM CONSOLE====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is :",balance)

    elif choice =="2":
        deposit = float(input("Enter the money to deposit :"))

        if deposit > 0:
            balance = balance + deposit
            print("Money Deposited")
        else:
            print("Enter a valid Amount")

    elif choice =="3":
        withdrawn = float(input("Enter the Amount to be withdrawn:"))
        if balance < withdrawn:
            print("Insufficient Funds in your Account.")
        else:
            if withdrawn>0:
                balance = balance - withdrawn
                print("The Amount has been debited")
            else:
                print("Enter a Valid Amount")
             

    elif choice == "4":
                print("Exiting the program.")
                break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")