# Define the path to the to-do list file
todo_file = "todo.txt"

# Function to display the to-do list
def show_todo_list():
    try:
        with open(todo_file, "r") as file:
            todo_list = file.readlines()
            if todo_list:
                print("To-Do List:")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your to-do list is empty.")
    except FileNotFoundError:
        print("No to-do list found. Create one by adding tasks.")

# Function to add a task to the to-do list
def add_task(task):
    with open(todo_file, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    try:
        with open(todo_file, "r") as file:
            lines = file.readlines()
        with open(todo_file, "w") as file:
            if 1 <= task_number <= len(lines):
                removed_task = lines.pop(task_number - 1)
                file.writelines(lines)
                print(f"Removed task: {removed_task.strip()}")
            else:
                print("Invalid task number.")
    except FileNotFoundError:
        print("No to-do list found. Nothing to remove.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Show to-do list")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        show_todo_list()
    elif choice == "2":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "3":
        show_todo_list()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
