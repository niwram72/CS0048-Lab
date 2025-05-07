import os
#############################################################
# MP1.1
foodAmount = 0

def pause(): # prompts input and clears screen
    input("Press Enter to continue...")

def discount(x):
    discountValue = x * 0.10  
    discountedPrice = x - discountValue
    return discountedPrice

def exit_confirmation(item_check): # checks user if they want to exit without ordering any items
    flag_pass = False # redundant kaya to?
    print("No orders placed! Are you sure you want to exit?")
    while not flag_pass: # Loops until user inputs the required characters    
        choice = input("Enter (y/n): ")     
        if choice.lower() == 'y':
            flag_pass = True
            return True
        elif choice.lower() == 'n':
            print("Returning to menu...\n")
            flag_pass = True
            return menu1()
        else:
            print("Invalid input. Enter only 'y' or 'n'.\n")

def menu1():
    global foodAmount
    while True:
        os.system('cls' if os.name =='nt' else 'clear')

        print("\n==== Welcome to Python Restaurant ====\n")
        print("\n==== Your Order ====")
        print("Menu: ")
        print("1. Burger - ₱120")
        print("2. Pizza - ₱300")
        print("3. Pasta - ₱250")
        print("4. Fries - ₱80")
        print("5. Exit")
        foodChoice = input("Select an item: ")
        
        if foodChoice == '1':
            foodAmount += 120
            print("Added Burger to your order.")
            pause()
        elif foodChoice == '2':
            foodAmount += 300
            print("Added Pizza to your order.")
            pause()
        elif foodChoice == '3':
            foodAmount += 250
            print("Added Pasta to your order.")
            pause()     
        elif foodChoice == '4':
            foodAmount += 80
            print("Added Fries to your order.")
            pause()         
        elif foodChoice == '5':
            discountedAmount = 0 ; finalAmount = 0 ; item_check = False
            
            if foodAmount == 0: # checks if there is not a single food item ordered, if otherwise it continues with computation
                checker = False
                checker = exit_confirmation(item_check)
                if checker == True:
                    print("Exiting...\n")     
                    break
            else:
                print("\n==== Order Summary ====\n")
                print(f"Total before discount: ₱{foodAmount}")
                if foodAmount > 500:
                    discountedAmount = discount(foodAmount)
                    print(f"Final Amount to Pay: ₱{discountedAmount}")
                else:
                    finalAmount = foodAmount
                    print(f"Final Amount to Pay: ₱{finalAmount}")
                pause()
                foodAmount = 0 # reset global var    
                break                
        else:
            print("Invalid input. Select a choice using numbers.")
# MP1.1
#############################################################


#############################################################
#MP1.2
cart = {} # initialize cart as dict
items = { # store's items in a dict
    "Rice": 50,
    "Eggs": 7,
    "Milk": 60,
    "Bread": 35
}

def view_items(): # print store items
    print("\n==== Available Items ====\n")
    print("Rice: ₱50")
    print("Eggs: ₱7")
    print("Milk: ₱60")
    print("Bread: ₱35\n")
    
    print("=========================\n")

def add_to_cart(cart, items):
    view_items()
    item = input("Enter item to add: ")
    
    matching_item = ""
    for inventory_item in items.keys():
        if inventory_item.lower() == item.lower():
            matching_item = inventory_item
            break
    
    if matching_item:
        try:
            quantity = int(input(f"Enter quantity for {matching_item}: "))
            if quantity > 0:
                if matching_item in cart:
                    cart[matching_item] += quantity
                else:
                    cart[matching_item] = quantity
                print(f"Added {quantity} {matching_item}(s) to cart.\n")
            else:
                print("Quantity must be positive.\n")
        except ValueError:
            print("Enter a valid number.\n")
    else:
        print(f"\n{item} is not on the list of items!\n")

def checkout(cart, items):
    subtotal = 0
    if not cart:
        print("Your cart is empty! Add an item first!\n")
        return
    print("\n==== Cart Summary ====")
    
    for item, quantity in cart.items():
        price = items[item]
        total = price * quantity
        subtotal += total
        print(f"\n{item} x {quantity} = ₱{total}")
        
    print(f"\nSubtotal: ₱{subtotal}")
    vat = subtotal * 0.12
    total_amount = subtotal + vat
    print(f"\nVAT (12%): ₱{vat}")
    print("======================")
    print(f"Total: ₱{total_amount}\n")    

def menu2():
    os.system('cls' if os.name =='nt' else 'clear')
    while True:
        print("==== Grocery Store ====\n")
        print("1. View Items")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit")
        print("\n=======================\n")
        storeChoice = input("What do you want to do?: ")

        if storeChoice == '1':
            view_items()
        elif storeChoice == '2':
            add_to_cart(cart, items)
        elif storeChoice == '3':  
            checkout(cart, items)
        elif storeChoice == '4':
            cart.clear()
            print("\nExiting Grocery Store...\n")    
            break
        else:
            print("Invalid input. Select a choice using numbers.")
# MP1.2
#############################################################

#############################################################
# MP1.3
total_steps = 0.00
calories = 0.00

def add_steps():
    global total_steps
    flag = False
    
    while not flag:
        try:
            new_steps = int(input("Enter the number of steps to add: "))
            if new_steps < 0:
                print("Please enter a positive number of steps.\n")
            else:
                total_steps += new_steps
                print(f"{new_steps} steps added. Total steps: {total_steps}\n")
                flag = True
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def view_total_steps():
    print(f"Total steps: {total_steps}\n")
    
def calories_burned():
    global calories, total_steps
    
    calories = total_steps * 0.04
    print(f"Calories Burned: {calories:.2f}\n")
    
def menu3():
    global total_steps, calories
    os.system('cls' if os.name =='nt' else 'clear')
    while True:
        print("==== Fitness Tracker Menu ====")
        print("1. Add Steps")
        print("2. View Total Steps")
        print("3. View Calories Burned")
        print("4. Exit")
        trackerChoice = input("Enter your choice (1-4): ")
        
        if trackerChoice == '1':
            add_steps()
        elif trackerChoice == '2':
            view_total_steps()
        elif trackerChoice == '3':
            calories_burned()
        elif trackerChoice == '4':
            total_steps = 0
            calories = 0
            print("Thank you for using the Fitness Tracker! Keep on staying healthy!\n")
            os.system('cls' if os.name =='nt' else 'clear')
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
# MP1.3
#############################################################


def main_menu():
    os.system('cls' if os.name =='nt' else 'clear')
    while True:
        print("==== Machine Problem 1: Main Menu ====\n")
        print("-    By Marwin Panganiban (TN21)     -\n")
        print("======================================\n\n")
        
        print("1. MP1.1 - Restaurant Order Management System")
        print("2. MP1.2 - Grocery Store Management System")
        print("3. MP1.3 - Fitness Tracker")
        print("4. Exit")
        
        program_choice = input("Enter the program you want to use: ")
        if program_choice == '1':
            menu1()
        elif program_choice == '2':
            menu2()
        elif program_choice == '3':
            menu3()
        elif program_choice == '4':
            print("Thank you for viewing my MP1 outputs!")
            break
        else:
            print("Please enter a valid numerical input.\n")
main_menu() # Start the program