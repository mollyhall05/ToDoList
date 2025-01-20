import json

def save_tasks(task_list, filename = "tasks.json"):
    with open(filename, "w") as f:
        json.dump(task_list, f)

def load_tasks(filename = "tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []