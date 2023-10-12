tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nCurrent List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Main program loo
while True:
    print("To-Do Menu:")
    print("1. Add the task")
    print("2. Remove the task")
    print("3. View the tasks")
    print("4. EXIT!!")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Please enter your task: ")
        add_task(task)
    elif choice == "2":
        task = input("Please enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
