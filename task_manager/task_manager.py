# task_manager.py

"""Module for managing tasks."""

class Task:
    """Represents a single task."""

    def __init__(self, title):
        """
        Initialize a Task instance.

        Args:
            title (str): The title of the task.
        """
        self.title = title
        self.completed = False

    def __str__(self):
        """Return a string representation of the task."""
        return f'Task(title="{self.title}", completed={self.completed})'


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self):
        """Initialize a TaskManager instance with an empty task list."""
        self.tasks = []

    def create_task(self, title):
        """
        Create a new task.

        Args:
            title (str): The title of the task to be created.

        Returns:
            Task: The created Task instance.
        """
        task = Task(title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        """List all tasks."""
        return self.tasks  # Return the list of tasks

    def delete_task(self, title):
        """Delete a task by title."""
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        """Mark a task as completed by title."""
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                break

    def get_task_titles(self):
        """Return a list of all task titles."""
        return [task.title for task in self.tasks]

    def get_completed_tasks(self):
        """Return a list of all completed tasks."""
        return [task for task in self.tasks if task.completed]

    def get_incomplete_tasks(self):
        """Return a list of all incomplete tasks."""
        return [task for task in self.tasks if not task.completed]

    def get_task_count(self):
        """Return the total number of tasks."""
        return len(self.tasks)

    def clear_completed_tasks(self):
        """Remove all completed tasks."""
        self.tasks = [task for task in self.tasks if not task.completed]

    def get_task_by_title(self, title):
        """Retrieve a task by its title."""
        for task in self.tasks:
            if task.title == title:
                return task
        return None  # Return None if the task is not found
