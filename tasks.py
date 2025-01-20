def create_task(description, completed = False):
    return {"description": description, "completed": completed}

def add_task(task_list, task):
    task_list.append(task)

def view_tasks(task_list):
    for i, task in enumerate(task_list):
        status = "Done" if task["completed"] else "Not done"
        print(f"{i+1}. {task['description']} - {status}")

def mark_task_complete(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True
    else:
        print("Invalid task index")