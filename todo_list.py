import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task.strip():
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        if not tasks[index].endswith("✔️"):
            tasks[index] += " ✔️"
            update_listbox()
    else:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

tk.Label(root, text="Enter Task:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()
