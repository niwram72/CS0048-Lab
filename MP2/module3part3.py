# initialize tasks as a dict
tasks = {}

def add_task(tasks):
    """User inputs task name and description, then stores in a dictionary"""

    task_name = input("Enter the task to add: ")
    task_desc = input("Enter description: ")            
    
    tasks[task_name] = task_desc
    print("Task successfully added.\n\n\n")

def remove_task(tasks):
    """Checks if list has contents, then user inputs task to remove"""
    
    if(len(tasks) == 0):
        print("List has no contents.\n\n\n")
        return
        
    while True:
        task_input = input("Enter task to remove (type EXIT to return to menu): ")
        if task_input in tasks:
            del tasks[task_input]
            print(f"Task {task_input} removed successfully.\n\n\n")
            break
        elif task_input == "EXIT":
            print("Returning to main menu...\n\n")
            break
        else:
            print("Task not in the list. Enter a valid task name (case sensitive).\n")

def view_tasks(tasks):
    """Simply retrieves and prints the values of the tasks dict"""
    
    if(len(tasks) == 0):
        print("List has no contents.\n\n\n")
        return  

    counter = 1
    for task_name, task_desc in tasks.items():
        print(f"== Task {counter} ==")
        print(f"{task_name}: {task_desc}\n")
        counter += 1
        
def run_menu():
    while True:
        # Display menu
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task")
        print("4. Exit")
        
        # Prompt the user to enter a choice
        choice = input("Enter a choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Thank you for using the To-Do List system!")
            break
        else:
            print("Enter a valid numerical input. Try again.")
    
run_menu()