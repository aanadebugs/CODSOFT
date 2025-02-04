tasks = []

def add_tasks(task):
    tasks.append({"task":task, "completed":False})
    print("Task added")

def list_tasks():
    print("\nTo-Do List")
    for index, task in enumerate(tasks, start=1):
        if task["completed"] :
            status = "✓"
        else :
            status = " "

        print(f"{index}. [{status}] {task['task']}")
    print()

def mark_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True 
        print("Task Marked as Complete")
    else: 
        print("Invalid task Index")

while True:
    print("\nOptions")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark as complete")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4):")

    if choice == "1":
        task = input("Enter the task: ")
        add_tasks(task)
    
    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()
        index = int(input("Enter the task number:"))
        mark_completed(index)

    elif choice == "4":
        print("Program Terminated")
        break

    else:
        print("Invalid choice. Please choose from 1,2,3 or 4")


                     