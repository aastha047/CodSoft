def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({'task': task, 'completed': False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task['completed'] else "."
            print(f"{i}. {task['task']} [{status}]")

def update_task(tasks):
    index = int(input("Enter the task number to update: ")) - 1
    if index < len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[index]['task'] = new_task
        print("Task updated!")
    else:
        print("Invalid task number.")

def mark_complete(tasks):
    index = int(input("Enter the task number to mark as complete: ")) - 1
    if index < len(tasks):
        tasks[index]['completed'] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

tasks = []
while True:
    print("\033[1m\033[4mA To-Do List Application: \033[0m\033[0m")
    print("1. Add a task\n2. View tasks\n3. Update a task\n4. Mark task as complete\n5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        update_task(tasks)
    elif choice == "4":
        mark_complete(tasks)
    elif choice == "5":
        print("Exiting the Appliation!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")

