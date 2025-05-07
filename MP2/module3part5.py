# initialize grades as a dict
grades = {}

def add_score(grades):
    # Prompt subject name & score
    subject_name = input("Enter subject name: ")
    
    while True:
        try:       
            subject_score = int(input("Enter score: "))
            break
        except:
            print("Enter a valid numerical input!\n\n")
    
    # Add the values to the dict
    grades[subject_name] = subject_score
    for subject, grade in grades.items():
        print(f"\n{subject}: {grade}")
    print("Score added.\n\n")

def calculate_avg(grades):
    if len(grades) == 0:
        print("No grades entered.\n\n\n")
        return
    
    average = sum(grades.values()) / len(grades)
    print(f"Average Grade: {average:.2f}\n\n\n")
    
def run_menu():
    while True:
        # Display menu
        print("===== Student Grade Calculator =====")
        print("1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")
        
        # Prompt user to enter their choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_score(grades)
        elif choice == '2':
            calculate_avg(grades)
        elif choice == '3':
            print("Thank you for using the Student Grade Calculator!")
            break
        else:
            print("Enter a valid numerical input. Try again.")
        
run_menu()