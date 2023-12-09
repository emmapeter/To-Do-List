# To-Do List Application in Python

# Function to display the to-do list
def display_todo_list():
    print("Your To-Do List:")
    with open("todo.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No tasks at the moment.")
        else:
            for i, task in enumerate(lines, 1):
                print(f"{i}. {task.strip()}")

# Function to add a task to the to-do list
def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task():
    display_todo_list()
    try:
        task_number = int(input("Enter the task number to remove: "))
        with open("todo.txt", "r") as file:
            lines = file.readlines()
        with open("todo.txt", "w") as file:
            for i, task in enumerate(lines, 1):
                if i != task_number:
                    file.write(task)
        print("Task removed successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main function to run the to-do list application
def main():
    while True:
        print("\nTo-Do List Application:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
