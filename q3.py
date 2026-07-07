tasks = []  
def show_menu():
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Exit")
def get_valid_command():
    while True:
        choice = input("Enter number (1-5): ").strip()

        if choice == "":
            print("ERROR: Input cannot be empty. Please enter a number.")
        elif not choice.isdigit():
            print("ERROR: '" + choice + "' is not valid. Enter a number between 1 and 5.")
        elif int(choice) < 1 or int(choice) > 5:
            print("ERROR: '" + choice + "' is out of range. Choose between 1 and 5.")
        else:
            return int(choice)
def get_valid_task():
    while True:
        task = input("Enter task name: ").strip()

        if task == "":
            print("ERROR: Task cannot be empty. Please try again.")
        elif len(task) < 3:
            print("ERROR: Task is too short. Please be more descriptive.")
        else:
            break

    print("\nSelect Priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    while True:
        choice = input("Enter number (1-3): ").strip()

        if choice == "":
            print("ERROR: Input cannot be empty.")
        elif not choice.isdigit():
            print("ERROR: '" + choice + "' is not valid. Enter 1, 2, or 3.")
        elif int(choice) < 1 or int(choice) > 3:
            print("ERROR: Out of range. Choose 1, 2, or 3.")
        else:
            choice = int(choice)
            if choice == 1:
                priority = "high"
            elif choice == 2:
                priority = "medium"
            else:
                priority = "low"
            return task, priority
def get_valid_number(action):
    while True:
        if len(tasks) == 0:
            print("ERROR: No tasks available to " + action + ".")
            return None

        num = input("Enter task number to " + action + ": ").strip()

        if num == "":
            print("ERROR: Task number cannot be empty.")
        elif not num.isdigit():
            print("ERROR: '" + num + "' is not a valid number.")
        elif int(num) < 1 or int(num) > len(tasks):
            print("ERROR: Out of range. Choose between 1 and " + str(len(tasks)) + ".")
        else:
            return int(num)
def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet.")
    else:
        print("\n  TO-DO LIST")
        for i in range(len(tasks)):
            status = "[Done]" if tasks[i]["completed"] else "[Pending]"
            priority = tasks[i]["priority"].upper()
            name = tasks[i]["name"]
            print(str(i + 1) + ". " + name + " - " + priority + " " + status)
# MAIN PROGRAM
print("=" * 40)
print("    WELCOME TO TO-DO LIST MANAGER")
print("=" * 40)

while True:
    show_menu()
    command = get_valid_command()

    if command == 5:
        break

    elif command == 1:
        task_name, priority = get_valid_task()
        tasks.append({"name": task_name, "priority": priority, "completed": False})
        print("Task added: " + task_name + " [" + priority + "]")

    elif command == 2:
        show_tasks()

    elif command == 3:
        show_tasks()
        num = get_valid_number("delete")
        if num is not None:
            removed = tasks[num - 1]
            tasks.pop(num - 1)
            print("Deleted: " + removed["name"])

    elif command == 4:
        show_tasks()
        num = get_valid_number("complete")
        if num is not None:
            if tasks[num - 1]["completed"] == True:
                print("ERROR: Task '" + tasks[num - 1]["name"] + "' is already done.")
            else:
                tasks[num - 1]["completed"] = True
                print("Marked as complete: " + tasks[num - 1]["name"])

#Final Summary
completed = 0
pending = 0
for task in tasks:
    if task["completed"] == True:
        completed = completed + 1
    else:
        pending = pending + 1

print("\n FINAL SUMMARY ")
print("Total Tasks:     " + str(len(tasks)))
print("Completed Tasks: " + str(completed))
print("Pending Tasks:   " + str(pending))

if len(tasks) > 0:
    print("\nFull Task List:")
    for i in range(len(tasks)):
        status = "[Done]" if tasks[i]["completed"] else "[Pending]"
        print("  " + str(i + 1) + ". " + tasks[i]["name"] + " - " + tasks[i]["priority"] + " " + status)
print("Goodbye!")