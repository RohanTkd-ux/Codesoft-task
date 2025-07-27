import json
import os

FILENAME = "tasks.json"

# Load tasks from a file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to a file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Create a task
def add_task(tasks):
    title = input("Enter new task: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("✅ Task created successfully.")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new task title: ")
            tasks[index]["title"] = new_title
            save_tasks(tasks)
            print("✏ Task updated successfully.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Mark task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as complete.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Track (View) all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

# Delete a task (optional)
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 Task '{deleted['title']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Create Task")
        print("2. Update Task")
        print("3. Mark Task as Complete")
        print("4. Track Tasks (View)")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❗ Invalid option. Please choose between 1 and 6.")

if _name_ == "_main_":
    main()




