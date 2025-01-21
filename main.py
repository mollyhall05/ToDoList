import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tasks import create_task, add_task, view_tasks, mark_task_complete
from storage import save_tasks, load_tasks

def main():

    # create the main GUI window
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("400x400")
    root.iconbitmap("Desktop/todolist-python/icon.ico")
    root.configure(bg="#f0f0f0")
    style.theme_use("clam")

    task_list = load_tasks()

    # functions 
    def add_task():
        description = task_input.get()
        if description:
            task = create_task(description)
            task_list.append(task)
            task_listbox.insert(tk.END, description)
            task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Enter task description")

    def delete_task():
        try:
            selected_index = task_listbox.curselection()[0]
            task_list.pop(selected_index)
            task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Select a task")
    
    def mark_task_completed():
        try:
            selected_index = task_listbox.curselection()[0]
            task_list[selected_index]["completed"] = True
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, task_list[selected_index]["description"] + " - Done")
        except IndexError:
            messagebox.showwarning("Select a task")

    def save_to_file():
        save_tasks(task_list)
        messagebox.showinfo("Tasks saved")

    # text box to enter task description
    task_input = ttk.Entry(root, width=40)
    task_input.pack(pady=10, padx=10, anchor="center")

    #'add task' button
    add_task_button = ttk.Button(root, text="Add task", command=add_task)
    add_task_button.pack(pady=5, padx=10, anchor="center")

    # 'delete task' button
    delete_task_button = ttk.Button(root, text="Delete task", command=delete_task)
    delete_task_button.pack(pady=5)

    # 'mark task completed' button
    mark_complete_button = ttk.Button(root, text="Mark task completed", command=mark_task_completed)
    mark_complete_button.pack(pady=5)

    # 'save tasks' button
    save_button = ttk.Button(root, text="Save tasks", command=save_to_file)
    save_button.pack(pady=5)

    # display the existing tasks
    task_listbox = ttk.Treeview(root, columns=("Task"), show="headings", height=15)
    task_listbox.heading("Task", text="Tasks")
    task_listbox.column("Task", anchor="w")
    task_listbox.pack(pady=10, padx=10, anchor="center")

    for task in task_list:
        description = task["description"]
        if task["completed"]:
            description += " (Done)"
        task_listbox.insert(tk.END, description)

    root.mainloop()

if __name__ == "__main__":
    main()