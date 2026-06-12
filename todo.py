tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter your task: ")

        task = {
            "id": len(tasks) + 1,
            "task": task_name
        }

        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for t in tasks:
                print(t["id"], t["task"])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")