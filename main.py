from tasks import create_task, add_task, view_tasks, mark_task_complete
from storage import save_tasks, load_tasks

def main():
    task_list = load_tasks()
    while True:
        print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Save and exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description:")
            add_task(task_list, create_task(description))
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            view_tasks(task_list)
            index = int(input("Enter task index to mark as complete: ")) - 1
            mark_task_complete(task_list, index)
        elif choice == "4":
            save_tasks(task_list)
            print("Tasks saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()