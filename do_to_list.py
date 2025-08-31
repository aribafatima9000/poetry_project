# Simple To-Do List Program

tasks = []  # empty list to store tasks

def show_menu():
    print("\n==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added!")

    elif choice == "2":
        if not tasks:
            print("⚠ No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("⚠ No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"🗑 Task '{removed}' removed!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please try again.")
