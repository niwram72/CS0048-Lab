# 1. Display a list of available items and their prices.
# 2. Allow users to add items to their cart and specify quantities.
# 3. Calculate the subtotal, VAT, and total amount during checkout.
# 4. Use if-elif statements to handle menu choices and item tracking.

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

menu2() # Start the program