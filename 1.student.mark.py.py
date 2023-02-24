def total_student():
    return int(input(f"Enter number of student: "))


def student_info():
    ID = input("Enter the student id: ")
    name = input("Enter the name of student: ")
    DoB = input("Enter the DoB: ")
    sif.append((ID, name, DoB))


def total_course():
    return int(input(f"Enter number of course: "))


def course_info():
    ID = input("Enter the course ID: ")
    name = input("Enter the course: ")
    cif.append((ID, name))


def list_student(students):
    for student in students:
        print("Student's name:", student[1])
        print("ID:", student[0])
        print("DOB:", student[2])


def list_course(courses):
    for course in courses:
        print("Course's name:", course[1])
        print("ID:", course[0])


def select(courses, students):
    for course in courses:
        for student in students:
            print("Course's name:", course[1])
            print("Student's name:", student[1])
            mark = int(input())
            print("Mark:", mark)

sif = []
cif = []
ts, cs = 0, 0
mark = []
while True:
    print("""
Welcome to the student managament system! Please choose an option as below:
    0. Exit
    1. Input number of students
    2. Input students information (ID, name, DoB)
    3. Input number of courses
    4. Input course information (ID, name)
    5. List student
    6. List courses
    7. Input marks for student in a course""")
    selection = int(input())
    if selection == 0:
        break
    elif selection == 1:
        ts = total_student()
    elif selection == 2:
        student_info()
    elif selection == 3:
        cs = total_course()
    elif selection == 4:
        course_info()
    elif selection == 5:
        list_student(sif)
    elif selection == 6:
        list_course(cif)
    elif selection == 7:
        select()
    else:
        print("Please try again!")
