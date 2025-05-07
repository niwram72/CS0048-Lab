# Convert C to F, and F to C
def celsius_to_fahrenheit(num):
    result = ( (num * (9/5)) + 32)
    return result

def fahrenheit_to_celsius(num):
    result = ( (num - 32) * (5/9) )
    return result

num = 0
def run_tempconverter():
    global num
    result = 0
    while True:
        isValidInput = False
        # Display menu
        print("===== Temperature Converter =====")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        
        # Prompt user to enter their choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while isValidInput == False:
                try:
                    num = float(input("Enter the degrees in Celsius: "))
                    result = celsius_to_fahrenheit(num)
                    print(f"The temperature in Fahrenheit is: {result:.2f}\n\n\n")
                    isValidInput = True
                except ValueError:
                    print("Enter a valid numerical input!\n\n")
        elif choice == '2':
            while isValidInput == False:
                try:
                    num = float(input("Enter the degrees in Fahrenheit: "))
                    result = fahrenheit_to_celsius(num)
                    print(f"The temperature in Celsius is: {result:.2f}")
                    isValidInput = True
                except ValueError:
                    print("Enter a valid numerical input!\n\n")
        elif choice == '3':
            print("Thank you for using the Temperature Converter!")
            break
        else:
            print("Enter a valid numerical input. Try again.")

run_tempconverter()