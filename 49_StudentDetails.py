import csv

FILENAME = "students.csv"

# --- Helper Functions ---

def load_students():
    students = []
    try:
        with open(FILENAME, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            students = list(reader)
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open(FILENAME, mode="w", newline='') as file:
        fieldnames = ["ID", "Name", "Age", "Course"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(students):
    print("\n--- Add New Student ---")
    ID = input("Enter ID: ")
    Name = input("Enter Name: ")
    Age = input("Enter Age: ")
    Course = input("Enter Course: ")

    students.append({"ID": ID, "Name": Name, "Age": Age, "Course": Course})
    save_students(students)
    print("Student added successfully!")

def view_students(students):
    print("\n--- Student Records ---")
    if not students:
        print("No student data found!")
        return
    for s in students:
        print(f"ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Course: {s['Course']}")

def search_student(students):
    key = input("\nEnter student ID or Name to search: ")
    found = [s for s in students if s['ID'] == key or s['Name'].lower() == key.lower()]
    if found:
        for s in found:
            print(f"Found → ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Course: {s['Course']}")
    else:
        print("No record found.")

def update_student(students):
    key = input("\nEnter ID of student to update: ")
    for s in students:
        if s['ID'] == key:
            print("Leave blank to keep old value.")
            new_name = input(f"Enter new name ({s['Name']}): ") or s['Name']
            new_age = input(f"Enter new age ({s['Age']}): ") or s['Age']
            new_course = input(f"Enter new course ({s['Course']}): ") or s['Course']
            s.update({"Name": new_name, "Age": new_age, "Course": new_course})
            save_students(students)
            print("Record updated successfully!")
            return
    print("Student not found.")

def delete_student(students):
    key = input("\nEnter ID of student to delete: ")
    for s in students:
        if s['ID'] == key:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

# --- Main Menu ---
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. View All Students")
        print("2. Add New Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            view_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
