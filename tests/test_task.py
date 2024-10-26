# tests/test_task.py

"""Unit tests for the TaskManager and Task classes."""

import pytest
from task_manager.task_manager import Task, TaskManager

@pytest.fixture
def create_task_manager():
    """Fixture to create a TaskManager instance."""
    return TaskManager()

def test_create_task(task_manager_instance):
    """Test the creation of a task."""
    task_title = "Test Task"
    task = task_manager_instance.create_task(task_title)
    assert isinstance(task, Task)  # Check if the created task is an instance of Task
    assert task.title == task_title  # Check if the title is set correctly
    assert not task.completed  # Check if the task is initially not completed

def test_create_task2(task_manager_instance):
    """Test the creation of a task."""
    task_title = "Test Task"
    task = task_manager_instance.create_task(task_title)
    assert isinstance(task, Task)  # Check if the created task is an instance of Task
    assert task.title == task_title  # Check if the title is set correctly
    assert not task.completed  # Check if the task is initially not completed
