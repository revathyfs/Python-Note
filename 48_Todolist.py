# To-Do List Project with File Handling

FILENAME = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main Program
def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark complete: "))
                tasks[task_num - 1] += " (Completed)"
                save_tasks(tasks)
                print("Task marked as complete!")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "4":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                deleted = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Deleted task: {deleted}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
