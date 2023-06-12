import tkinter as tk
from tkinter import messagebox, simpledialog
from checkbox_listbox import CheckboxListbox


class TodoAppGUI:
    def __init__(self, backend):
        self.backend = backend
        self.window = tk.Tk()
        self.window.title("Todo App")

        self.task_listbox = CheckboxListbox(self.window)
        self.task_listbox.pack()

        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Add close box ("X") to the top right of the window
        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)

        self.update_task_list()

        # Set the window size
        self.window.geometry("200x200")

    def update_task_list(self):
        self.task_listbox.delete(0)
        tasks = self.backend.get_tasks()
        for task in tasks:
            self.task_listbox.insert(task)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.backend.add_task(task)
            messagebox.showinfo("Success", "Task added successfully!")
            self.update_task_list()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        checked_indices = self.task_listbox.get_checked_indices()
        if not checked_indices:
            messagebox.showinfo("No Tasks Selected", "No tasks selected.")
        else:
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected task(s)?")
            if confirmation:
                indices_to_delete = reversed(checked_indices)
                for index in indices_to_delete:
                    self.backend.delete_task(index)
                messagebox.showinfo("Success", "Task(s) deleted.")
                self.update_task_list()

    def run(self):
        self.window.mainloop()
