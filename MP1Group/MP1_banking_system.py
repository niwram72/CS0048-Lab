def deposit(amount, transaction_history):
    """Adds the deposit amount to the balance, and store the transaction details to transaction_history list"""
    global balance
    total = amount
    balance += total
    print(f"Deposited ${total:.2f}\nCurrent balance is: ${balance:.2f}")
    # Map values as dictionary mapping to lists
    transaction_history.setdefault("Deposited", []).append(total)

def withdraw(amount, transaction_history):
    """Deducts the withdrawal amount to the balance, transaction_history is updated"""
    global balance
    total = amount
    balance -= total
    print(f"Withdrew ${total:.2f}\nCurrent balance is: ${balance:.2f}")
    
    transaction_history.setdefault("Withdrew", []).append(total)
    
def check_balance(transaction_history):
    """Calls and prints the global var balance and record users' action in transaction_history"""
    global balance
    print(f"Your current balance is: ${balance:.2f}\n\n")
    
    transaction_history.setdefault("Checked balance", []).append("")
    
def summary(transaction_history):
    """Checks if list has content, then traverse through the list to print the transaction logs of the user"""
    if(len(transaction_history) == 0):
        print("No transactions performed.")
    
    print("\nSummary of transactions:\n")
    for operation, values in transaction_history.items():
        for value in values:
            if value == "":
                print(f"{operation}\n")
            else:
                print(f"{operation}: {value}\n")
    print("Thank you for using the banking system!")

def banking_system():
    """Main menu of the system. Prompts and input validation are performed here."""
    ZERO = 0
    global balance
    transaction_history = {}
    while True:
        inputCheck = False
        print("\n===== Banking System =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("==========================")
        choice = input("Enter choice: ")
        
        if choice == '1':
            while inputCheck == False:
                amount_str = input("Enter amount to deposit: ")
                try:
                    amount = float(amount_str)
                    if(amount < 0):
                        print("Invalid amount. Please enter a positive number.")
                        transaction_history.setdefault("Attempted to deposit ", []).append(amount)
                    else:                        
                        inputCheck = True
                        deposit(amount, transaction_history)
                except ValueError:
                    print("Invalid characters entered. Enter a valid numerical input!\n")
                    transaction_history.setdefault("Attempted to deposit", []).append(f'"{amount_str}" (declined)')                                
        elif choice == '2':
            # if balance <= ZERO:
            #     print("You cannot withdraw if you don't have money in your account!\n")
            #     transaction_history.setdefault("Attempted to withdraw", []).append("with zero balance (declined)")
            #     continue
            
            while inputCheck == False:
                amount_str = input("Enter amount to withdraw: ")
                try:
                    amount = float(amount_str)
                    if(amount > balance):
                        print("You cannot withdraw more than your current balance!\n")
                        transaction_history.setdefault("Attempted to withdraw", []).append(f"{amount_str} (declined)")
                        break
                    elif(amount < 0):
                        print("Invalid amount. Please enter a positive number.")
                        transaction_history.setdefault("Attempted to withdraw", []).append(f'"{amount_str}" (declined)')
                    elif(amount == 0):
                        print("Invalid amount. Please enter a positive number.")
                        transaction_history.setdefault("Attempted to withdraw", []).append(f"{amount_str} (declined)")
                        break        
                    else:
                        inputCheck = True
                        withdraw(amount, transaction_history)                        
                except ValueError:
                    print("Invalid characters entered. Enter a valid numerical input!\n")
                    transaction_history.setdefault("Attempted to withdraw", []).append(f'"{amount_str}" (declined)')
                    break
        elif choice == '3':
            check_balance(transaction_history)
        elif choice == '4':
            summary(transaction_history)
            break
        else:
            print("Invalid input. Enter a valid numerical input.")        

# Prompt user for intial balance
initialCheck = False
print("===== Welcome to the Banking System =====\n")

while initialCheck == False:
    try:      
        balance = float(input("\nEnter your initial balance: "))
        initialCheck = True
        banking_system()
    except ValueError:
        print("Invalid characters entered. Enter a valid numerical input!\n")