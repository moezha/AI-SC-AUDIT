"""
Unit tests for the TaskManager and Task classes.
"""

from task_manager.task_manager import Task, TaskManager


def test_create_task():
    task_manager_fixture_instance=TaskManager()
    """Test the creation of a task."""
    task_title = "Test Task"
    task = task_manager_fixture_instance.create_task(task_title)
    assert isinstance(task, Task)
    assert task.title == task_title
    assert not task.completed
