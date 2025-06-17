class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, price, quantity)
        return f'Added x{quantity} {name} to the cart.'

    def remove_product(self, name, quantity):
        if name in self.products:
            if self.products[name].quantity <= quantity:
                del self.products[name]
                return f'Removed {name} from the cart.'
            else:
                self.products[name].quantity -= quantity
                return f'Removed x{quantity} "{name}".'
        return f'Product {name} not found in cart.'

    def view_cart(self):
        if not self.products:
            return "Your cart is empty."
        return "\n".join(str(product) for product in self.products.values())

    def checkout(self):
        total = sum(product.price * product.quantity for product in self.products.values())
        self.products.clear()
        return f'Total price: P{total:.2f}\nCheckout complete!'

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} - P{self.price:.2f} x {self.quantity}'

def main():
    cart = ShoppingCart()

    while True:
        print("\nOnline Shopping Cart")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
            print(cart.add_product(name, price, quantity))
        elif choice == '2':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity to remove: "))
            print(cart.remove_product(name, quantity))
        elif choice == '3':
            print(cart.view_cart())
        elif choice == '4':
            print(cart.checkout())
        elif choice == '5':
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()