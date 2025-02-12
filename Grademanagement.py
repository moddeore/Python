student_grade = { }

#add the student
def add_student(name,grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")

#update the student
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are added {grade}")

    else:
        print("Student not found!!")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f'{name} has been delected!')

    else:
        print("Not found !!")

#for viewing
def view_all():
    if student_grade:
        for name , grade in student_grade.items():
            print(f'{name} = {grade}')
    
    else:
        print("No Student ADDED !!")

def main():
    while True:
        print("!! Student Grade Managemant !!")
        print("1.Add Student")
        print("2.Update Student")
        print("3.Delete Student")
        print("4.View Student")
        print("5.Exit")

        work = int(input("Enter the work : "))

        if work == 1:
            name = input("Enter the name : ")
            grade = int(input("Enter the grade : "))
            add_student(name,grade)
        elif work == 2:
            name = input("Enter the student name : ")
            grade = int(input("Enter updated grade : "))
            update_student(name,grade)

        elif work == 3:
            name = input("Enter the student name : ")
            delete_student(name)

        elif work == 4:
            view_all()
        
        elif work == 5:
            print("Programm is CLOSSING !!")
            break
        else:
            print("Invalid Choice !")

