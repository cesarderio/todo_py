import tkinter as tk

class CheckboxListbox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.checkboxes = []
        self.tasks = []

    def insert(self, task):
        self.tasks.append(task)
        checkbox = tk.Checkbutton(self, text=task)
        checkbox.pack(anchor="w", side="top")
        self.checkboxes.append(checkbox)

    def delete(self, index):
        if index < len(self.tasks):
            self.tasks.pop(index)
            checkbox = self.checkboxes.pop(index)
            checkbox.destroy()

    def get_checked_indices(self):
        return [index for index, checkbox in enumerate(self.checkboxes) if checkbox.getvar(tk.IntVar()).get() == 1]

    def get_task(self, index):
        return self.tasks[index]
