print("Welcome to the To-Do List Application!")


def ensure_file():
    try:
        open("tasks.txt", "a").close()
    except Exception:
        pass


def add_task():
    task = input("Enter the task you want to add: ").strip()
    if task:
        with open("tasks.txt", "a", encoding="utf-8") as file:
            file.write(task + "\n")
        print(f'Task "{task}" has been added to your to-do list.')
    else:
        print("No task entered. Nothing was added.")


def remove_task():
    task = input("Enter the task you want to remove: ").strip()
    if not task:
        print("No task entered. Nothing was removed.")
        return
    with open("tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    new_lines = [line for line in lines if line.strip() != task]
    if len(new_lines) == len(lines):
        print(f'Task "{task}" was not found in your to-do list.')
    else:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            file.writelines(new_lines)
        print(f'Task "{task}" has been removed from your to-do list.')


def view_tasks():
    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = [t.strip() for t in file.readlines() if t.strip()]
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")


ensure_file()
while True:
    print("\nWhat would you like to do today? add, remove, view, or quit")
    user_choice = input("Enter your choice: ").strip().lower()
    if user_choice == "add":
        add_task()
    elif user_choice == "remove":
        remove_task()
    elif user_choice == "view":
        view_tasks()
    elif user_choice == "quit" or user_choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'add', 'remove', 'view', or 'quit'.")