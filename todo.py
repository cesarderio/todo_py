import os

# display main menu options
def show_menu():
    print()
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")
    print()

# print tasks
def print_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")
    print_tasks()

# view all the tasks
def view_tasks():
    print_tasks()

# mark task as complete
def mark_task_complete():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            save_tasks()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# delete a task
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            confirmation = input("Are you sure you want to delete this task? (y/n): ")
            if confirmation.lower() == 'y':
                tasks.pop(task_index)
                save_tasks()
                print("Task deleted.")
            else:
                print("Deletion canceled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# save tasks to a file
def save_tasks():
    try:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except IOError:
        print("Error occurred while saving tasks.")

# load tasks from a file
def load_tasks():
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    task = line.strip()
                    if task:
                        tasks.append(task)
        except IOError:
            print("Error occurred while loading tasks.")
    else:
        try:
            with open(file_path, 'w') as file:
                print("Created a new task file.")
        except IOError:
            print("Error occurred while creating the task file.")

# clear the console screen
def clear_screen():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix/Linux/Mac
        os.system('clear')

# Main 
file_path = 'tasks.txt'
tasks = []
load_tasks()

print("Welcome to the Todo App!")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    clear_screen()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
