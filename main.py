students =[]


def add_student():
    id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }
    
    students.append(student)
    print("Students Added Successsfully")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("ID:", student["id"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])
            print("-----------------------")

def search_student():
    search_id = int(input("Enter Student ID to Search: "))

    found = False

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])

            found = True
            break

    if not found:
        print("Student Not Found")

def update_student():
    update_id = int(input("Enter Student ID to Update: "))

    found = False

    for student in students:
        if student["id"] == update_id:

            student["Name"] = input("Enter New Name: ")
            student["Age"] = int(input("Enter New Age: "))
            student["Course"] = input("Enter New Course: ")
            student["Marks"] = float(input("Enter New Marks: "))

            print("Student Updated Successfully")

            found = True
            break

    if not found:
        print("Student Not Found")

def delete_student():
    delete_id = int(input("Enter Student ID to Delete: "))

    found = False

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student Deleted Successfully")
            found = True
            break

    if not found:
        print("Student Not Found")



while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

        
add_student()
view_students()
search_student()
update_student()
delete_student()

