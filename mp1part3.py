# The goal of this machine problem is to create a program to simulate a fitness tracker. 
# Users can add steps to their total step count, view their total steps, and calculate the calories burned based on their steps.

# Requirements:
# Provide a menu with the following options:
# Add Steps: Allow the user to add steps to their total step count. !!!!!
# View Total Steps: Display the total number of steps added so far. !!!!!
# View Calories Burned: Calculate and display the calories burned based on the total steps (assume 0.04 calories per step). !!!!!!!
# Exit: End the program with a friendly message. !!!!!
# Track the total number of steps using a single variable. !!!!!1
# Use the formula calories = steps * 0.04 to calculate calories burned. !!!!!
# Provide clear feedback after each operation. 
# Handle invalid inputs gracefully. !!!

# Features
# Allows users to add steps to their total step count. !!!!!!!!
# Displays the total number of steps added so far. !!!!
# Calculates and displays the calories burned based on the total steps. !!!!!!
# Provides a user-friendly interface with clear feedback. 
# Handles invalid inputs gracefully. !!!!!

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
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
menu3() # Start the program