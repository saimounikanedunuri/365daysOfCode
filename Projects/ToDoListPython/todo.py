import os

# File to store tasks
TASKS_FILE = "tasks.txt"


# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added successfully.')


# Complete a task
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to mark as complete: ")) - 1
        completed_task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f'Task "{completed_task}" marked as complete and removed from the list.')
    except (ValueError, IndexError):
        print("Invalid task number.")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to delete: ")) - 1
        deleted_task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f'Task "{deleted_task}" deleted from the list.')
    except (ValueError, IndexError):
        print("Invalid task number.")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
