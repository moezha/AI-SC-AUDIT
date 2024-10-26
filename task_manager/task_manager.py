class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

class TaskManager:
    def create_task(self, title):
        return Task(title)
