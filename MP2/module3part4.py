import random

def run_game():
    attempts = 0
    # Generate a random number between 1 - 100.    
    random_number = random.randint(1, 100)
    # print(f"The number is: {random_number}")
    
    # Prompt user to guess the number
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            if guess > random_number:
                print("Too high!")
                attempts += 1
            elif guess < random_number:
                print("Too low!")
                attempts += 1
            elif guess == random_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.\n\n\n")
                break
            else:
                print("This is an else statement")
        except ValueError:
            print("Enter a valid numerical input!")

def game_menu():
    while True:
        # Display menu
        print("===== Number Guessing Game =====")
        print("1. Play Number Guessing Game")
        print("2. Exit")
        
        # Prompt user to enter their choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # call game function
            run_game()            
        elif choice == '2':
            print("Thank you for playing the Number Guessing Game!")
            break
        else:
            print("Enter a valid numerical input.\n\n\n")

game_menu()