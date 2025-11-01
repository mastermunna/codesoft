import tkinter as tk
from tkinter import messagebox
import json
import os

# ------------------ File Handling ------------------
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# ------------------ Main App ------------------
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#e3f2fd")

        self.tasks = load_tasks()

        # ------------------ Widgets ------------------
        tk.Label(root, text="📝 TO-DO LIST", font=("Arial", 20, "bold"), bg="#e3f2fd").pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        add_btn = tk.Button(root, text="Add Task", command=self.add_task, bg="#42a5f5", fg="white", font=("Arial", 12))
        add_btn.pack(pady=5)

        self.listbox = tk.Listbox(root, font=("Arial", 12), height=15, selectmode=tk.SINGLE)
        self.listbox.pack(padx=20, pady=10, fill=tk.BOTH)

        complete_btn = tk.Button(root, text="Mark as Completed", command=self.mark_completed, bg="#66bb6a", fg="white", font=("Arial", 12))
        complete_btn.pack(pady=5)

        delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#ef5350", fg="white", font=("Arial", 12))
        delete_btn.pack(pady=5)

        self.refresh_tasks()

    # ------------------ Functions ------------------
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"title": task, "done": False})
            save_tasks(self.tasks)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display = f"{'✅ ' if task['done'] else '❌ '} {task['title']}"
            self.listbox.insert(tk.END, display)

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task to mark complete.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            save_tasks(self.tasks)
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task to delete.")

# ------------------ Run App ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
