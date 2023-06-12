import tkinter as tk
from tkinter import messagebox, simpledialog
from backend import TodoAppBackend


class CheckboxListbox(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.checkboxes = []
        self.tasks = []

    def add_task(self, task):
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(self, text=task, variable=checkbox_var)
        checkbox.pack(anchor="w")
        self.checkboxes.append((checkbox, checkbox_var))
        self.tasks.append(task)

    def delete(self, index):
        print(f"index: {index}, len(self.tasks): {len(self.tasks)}")
        if index == "all":
            self.tasks.clear()
        elif isinstance(index, int) and 0 <= index < len(self.tasks):
            del self.tasks[index]
        self.update_checkboxes()

    def update_checkboxes(self):
        for checkbox, _ in self.checkboxes:
            checkbox.destroy()
        self.checkboxes.clear()
        for task in self.tasks:
            checkbox_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self, text=task, variable=checkbox_var)
            checkbox.pack(anchor="w")
            self.checkboxes.append((checkbox, checkbox_var))

    def get_checked_indices(self):
        return [index for index, (_, checkbox_var) in enumerate(self.checkboxes) if checkbox_var.get() == 1]

    def get_task(self, index):
        return self.checkboxes[index][0].cget("text")


class TodoAppGUI:
    def __init__(self, backend):
        self.backend = backend
        self.window = tk.Tk()
        self.window.title("Todo App")

        self.top_frame = tk.Frame(self.window)
        self.top_frame.pack(side="top", fill="x")

        self.add_button = tk.Button(self.top_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left", padx=10, pady=5)

        self.delete_button = tk.Button(self.top_frame, text="Delete", command=self.delete_task)
        self.delete_button.pack(side="left", padx=10, pady=5)

        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.task_listbox = CheckboxListbox(self.canvas)
        self.task_listbox.pack(side="top", anchor="w")

        self.scrollbar = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.task_listbox, anchor="nw")

        self.task_listbox.bind("<Configure>", self.on_listbox_configure)

        # Add close box ("X") to the top right of the window
        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)

        self.update_task_list()

        # Set the window size
        self.window.geometry("305x225")

    def update_task_list(self):
        self.task_listbox.delete("all")  # Clear existing tasks
        tasks = self.backend.get_tasks()
        for task in tasks:
            self.task_listbox.add_task(task)


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
                indices_to_delete = list(reversed(checked_indices))
                for index in indices_to_delete:
                    task = self.task_listbox.get_task(index)
                    self.backend.delete_task(task)
                    self.task_listbox.delete(index)
                self.update_task_list()
                messagebox.showinfo("Success", "Task(s) deleted.")


    def on_listbox_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def run(self):
        self.window.mainloop()
