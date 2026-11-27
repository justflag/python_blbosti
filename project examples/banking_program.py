def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------------------------")
        print(" Welcome to banking program  ")
        print("---------------------------------")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("---------------------------------")

        print("---------------------------------")
        choice = input("Enter your choice (1-4): ")
        print("---------------------------------")

        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
            case _:
                print("Wrong input")

    print("---------------------------------")
    print("Thank you. Have a nice day.")
    print("---------------------------------")

if __name__ == '__main__':
    main()