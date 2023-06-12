import os

class TodoAppBackend:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def mark_task_complete(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            self.save_tasks()

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)


    def save_tasks(self):
        try:
            with open(self.file_path, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
        except IOError:
            print("An error occurred while saving tasks.")

    def load_tasks(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.tasks = [line.strip() for line in file.readlines() if line.strip()]
            except IOError:
                print("An error occurred while loading tasks.")
        else:
            try:
                with open(self.file_path, 'w') as file:
                    print("Created a new task file.")
            except IOError:
                print("An error occurred while creating the task file.")
