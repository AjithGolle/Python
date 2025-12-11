#python bank program
def show_balance(balance) :
    print(f"your balance is :{balance:.2f}")
def deposit() :
    amount = float(input("enter the amount to be deposited :"))

    if amount < 0 :
        print("the amount is not valid !")
        return 0
    else :
        return amount
def withdraw(balance) :
    amount = float(input("enter the amount to be withdraw :"))

    if amount > balance :
        print("insufficient funds !")
        return 0
    elif amount < 0 :
        print("amount must be greater than 0")
        return 0
    else :
        return amount

def main() :
    balance = 0
    is_running = True

    while is_running :
        print("*******************************")
        print("Banking program")
        print("*******************************")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")

        choice = input("enter your choice(1-4) :")
        if choice == '1' :
            show_balance(balance)
        elif choice == '2' :
            balance += deposit()
        elif choice == '3' :
            balance -= withdraw(balance)
        elif choice == '4' :
            is_running == False
        else :
            print("this is not a valid choice !")

    print("thank you !!!")

if __name__ == '__main__':
    main()