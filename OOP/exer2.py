class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}
    
    def add_grade(self, subject, grade):
        grade = float(grade)
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]
        return f'Added grade {grade} for {self.name} in {subject}.'
    
    def calculate_average(self):
        if not self.grades:
            return f'{self.name} has no grades recorded.'
        total_scores = sum(sum(map(float, scores)) for scores in self.grades.values())
        total_subjects = sum(len(scores) for scores in self.grades.values())
        return f'{self.name}\'s average grade: {total_scores / total_subjects:.2f}'
    
    def __str__(self):
        grade_info = "\n".join(f"{subject}: {scores}" for subject, scores in self.grades.items())
        return f'{self.name} - Grades:\n{grade_info if grade_info else "No grades added."}'

class GradeTracker:
    def __init__(self):
        self.students = {}
        
    def add_student(self, name):
        if name in self.students:
            return f'Student {name} already exists.'
        self.students[name] = Student(name)
        return f'Student "{name}" added.'
    
    def add_grade(self, name, subject, grade):
        if name in self.students:
            return self.students[name].add_grade(subject, grade)
        return f'Student "{name}" not found.'

    
    def calculate_average(self, name):
        if name in self.students:
            return self.students[name].calculate_average()
        return f'Student "{name}" not found.'
    
    def view_students(self):
        if not self.students:
            return "No students registered."
        return "\n".join(str(student) for student in self.students.values())

def main():
    record = GradeTracker()
    
    while True:
        print("\nStudent Grade Tracker")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Grades for a Student")
        print("4. Calculate Average")
        print("5. View all Students & Grades")
        print("6. Exit")
        
        choice = input("Enter choice 1-6: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            print(record.add_student(name))
        elif choice == '2':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            print(record.add_grade(name, subject, grade))
        elif choice == '3':
            name = input("Enter student name: ")
            if name in record.students:
                print(record.students[name])
            else:
                print(f'Student "{name}" not found.')
        elif choice == '4':
            name = input("Enter student name: ")
            print(record.calculate_average(name))
        elif choice == '5':
            print(record.view_students())
        elif choice == '6':
            print("Thank you for using the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()