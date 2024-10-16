class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

def add_task(tasks, title):
    new_id = len(tasks) + 1
    task = Task(new_id, title)
    tasks.append(task)

def view_tasks(tasks):
    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

def delete_task(tasks, task_id):
    tasks[:] = [task for task in tasks if task.id != task_id]

def complete_task(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True

import json

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []

def show_menu():
    print("\nMenu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

# Dummy login credentials
DUMMY_EMAIL = "abhi@gmail.com"
DUMMY_PASSWORD = "123"

def login():
    print("Login to Task Manager")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid email or password!")
        return False

def main():
    if login():  # Only proceed if login is successful
        tasks = load_tasks()
        while True:
            show_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                title = input("Enter task title: ")
                add_task(tasks, title)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            elif choice == '4':
                task_id = int(input("Enter task ID to mark as complete: "))
                complete_task(tasks, task_id)
            elif choice == '5':
                save_tasks(tasks)
                print("Tasks saved. Exiting.")
                break
            else:
                print("Invalid option. Try again.")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
