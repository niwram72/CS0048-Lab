# 1. Display a menu with predefined items.
# 2. Allow users to repeatedly select items until they choose to exit.
# 3. Calculate the total cost and apply discounts if applicable.
# 4. Do not use arrays, lists, or dictionaries to store the menu items.
# 5. Use if-elif statements to handle menu choices.

import os
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
    
menu1()  # Start the program