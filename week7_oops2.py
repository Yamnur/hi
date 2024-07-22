class Student:
    school_name = "govt high School"  # Class variable
    
    def __init__(self, name, usn, cgpa):
        self.name = name         # Instance attribute
        self.usn = usn           # Instance attribute
        self.cgpa = cgpa         # Instance attribute
        
    def calculate_grade(cgpa):
        if cgpa >= 9.0:
            return "O"
        elif cgpa >= 8.0:
            return "A"
        elif cgpa >= 7.0:
            return "B"
        elif cgpa >= 6.0:
            return "C"
        elif cgpa >= 5.0:
            return "D"
        else:
            return "F"
        
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"USN: {self.usn}")
        print(f"CGPA: {self.cgpa}")
        print(f"School Name: {self.school_name}")
        print()
        
    def delete_student(cls, students, usn):
        for i, student in enumerate(students):
            if student.usn == usn:
                del students[i]
                print(f"Student with USN {usn} deleted successfully.")
                return
        print(f"Student with USN {usn} not found.")
        
    def update_cgpa(cls, students, usn, new_cgpa):
        for student in students:
            if student.usn == usn:
                student.cgpa = new_cgpa
                print(f"CGPA updated successfully for {student.name}.")
                return
        print(f"Student with USN {usn} not found.")
        

# Interactive part
students = []

while True:
    print("\nStudent Management System Menu:")
    print("1. Add Student")
    print("2. Calculate Grade")
    print("3. Display Student Details by USN")
    print("4. Update CGPA by USN")
    print("5. Delete Student by USN")
    print("6. Display School Name")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        name = input("Enter student name: ")
        usn = input("Enter student USN: ")
        cgpa = float(input("Enter student CGPA: "))
        student = Student(name, usn, cgpa)
        students.append(student)
        print(f"Student {name} added successfully.")
        
    elif choice == '2':
        usn = input("Enter student USN to calculate grade: ")
        for student in students:
            if student.usn == usn:
                grade = Student.calculate_grade(student.cgpa)
                print(f"Grade for {student.name}: {grade}")
                break
        else:
            print(f"Student with USN {usn} not found.")
            
    elif choice == '3':
        usn = input("Enter student USN to display details: ")
        for student in students:
            if student.usn == usn:
                student.display_details()
                break
        else:
            print(f"Student with USN {usn} not found.")
            
    elif choice == '4':
        usn = input("Enter student USN to update CGPA: ")
        new_cgpa = float(input("Enter new CGPA: "))
        Student.update_cgpa(students, usn, new_cgpa)
        
    elif choice == '5':
        usn = input("Enter student USN to delete: ")
        Student.delete_student(students, usn)
        
    elif choice == '6':
        print(f"School Name: {Student.school_name}")
        
    elif choice == '7':
        print("Exiting Student Management System.")
        break
    
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
