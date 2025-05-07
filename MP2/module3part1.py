def addition(num1, num2):
    """Performs addition of two numbers"""
    result = num1 + num2
    return result

def subtraction(num1, num2):
    """Performs subtraction of two numbers"""
    result = num1 - num2
    return result

def multiplication(num1, num2):
    """Performs multiplication of two numbers"""
    result = num1 * num2
    return result

def division(num1, num2):
    """Performs division of two numbers"""
    result = num1 / num2
    return result

def run_calculator():
    while True:
        # Reset variables
        num1 = 0; num2 = 0; output = 0;
        # Display menu
        print("===== Calculator Menu =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Prompt user to enter their choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            output = addition(num1, num2)
            print(f"The result is: {output:.2f}\n\n\n")
        elif choice == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            output = subtraction(num1, num2)
            print(f"The result is: {output:.2f}\n\n\n")            
        elif choice == '3':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            output = multiplication(num1, num2)
            print(f"The result is: {output:.2f}\n\n\n")            
        elif choice == '4':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            output = division(num1, num2)
            print(f"The result is: {output:.2f}\n\n\n")
        elif choice == '5':
            print("Thank you for using the Calculator System!")
            break
        else:
            print("Enter a valid numerical input. Try again.")
        
run_calculator()