import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TaskWidget(tk.Frame):
    def __init__(self, parent, task_text, delete_callback, edit_callback):
        super().__init__(parent)
        self.pack(fill="x")
        self.task_text = task_text

        self.label = tk.Label(self, text=task_text, width=50)
        self.label.pack(side="left", padx=(10, 5))

        self.edit_button = tk.Button(self, text="Edit", command=edit_callback, bg="#FFA000", fg="white")
        self.edit_button.pack(side="left", padx=(0, 5))

        self.delete_button = tk.Button(self, text="Delete", command=delete_callback, bg="#D32F2F", fg="white")
        self.delete_button.pack(side="left")

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(background="#f0f0f0")

    
        header_label = tk.Label(root, text="To-Do List", font=("Arial", 20), bg="#4CAF50", fg="white")
        header_label.grid(row=0, column=0, columnspan=3, pady=10)

        
        self.tasks = []

        
        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        
        self.task_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.task_entry.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

      
        add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#388E3C", fg="white")
        add_button.grid(row=2, column=2, padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            task_widget = TaskWidget(self.tasks_frame, task_text, self.delete_task, lambda: self.edit_task(task_widget))
            self.tasks.append(task_widget)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        task_widget = self.root.focus_get().master
        task_widget.destroy()
        self.tasks.remove(task_widget)

    def edit_task(self, task_widget):
        new_task_text = simpledialog.askstring("Edit Task", "Enter new task:", initialvalue=task_widget.task_text)
        if new_task_text:
            task_widget.label.config(text=new_task_text)
            task_widget.task_text = new_task_text

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()