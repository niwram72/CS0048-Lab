def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number!")
                continue
            return value
        except ValueError:
            print("Invalid input! please enter a valid number")

walkNum = 5
runNum = 10
cycleNum = 8
swimNum = 12
totalCalorie = 0

activity_minutes = {"walking": 0, "running": 0, "cycling": 0, "swimming": 0}

print("=====Fitness Tracker=====")

weight = get_positive_int("Enter Your Current Weight: ")

while True:
    print("=====Enter Activity Type=====")
    print("(1) Walking")
    print("(2) Running")
    print("(3) Cycling")
    print("(4) Display total Calories Burned and Exit")
    activity = input("Choice: ").strip()

    if activity == "1":
        minutes = get_positive_int("Enter Duration(minutes): ")
        activity_minutes["walking"] += minutes
    elif activity == "2":
        minutes = get_positive_int("Enter Duration(minutes): ")
        activity_minutes["running"] += minutes
    elif activity == "3":
        minutes = get_positive_int("Enter Duration(minutes): ")
        activity_minutes["cycling"] += minutes
    elif activity == "4":
        break
    else:
        print("Invalid Choice! Please try again!")
        continue

    user_input = input("Enter 1 to add another or press any key to finish: ").strip()
    
    if user_input != '1':
        break

#output
print("\nActivity Summary")
if activity_minutes["walking"]:
    calories = int(activity_minutes["walking"] * walkNum * (weight / 70))
    print(f"Calories Burned for Walking = {calories} Calories")
    totalCalorie += calories

if activity_minutes["running"]:
    calories = int(activity_minutes["running"] * runNum * (weight / 70))
    print(f"Calories Burned for Running = {calories} Calories")
    totalCalorie += calories
    
if activity_minutes["cycling"]:
    calories = int(activity_minutes["cycling"] * cycleNum * (weight / 70))
    print(f"Calories Burned for Cycling = {calories} Calories")
    totalCalorie += calories

if activity_minutes["swimming"]:
    calories = int(activity_minutes["swimming"] * swimNum * (weight / 70))
    print(f"Calories Burned for Swimming = {calories} Calories")
    totalCalorie += calories

print(f"Total Calories Burned Today = {totalCalorie} Calories")

if totalCalorie >= 500:
    print("Congratulations for burning more than 500 calories today!")