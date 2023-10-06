from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from .models import Task

class ToDoListTest(TestCase):
    def setUp(self):
        # Create some sample tasks for testing
        Task.objects.create(title="Task 1", completed=False)
        Task.objects.create(title="Task 2", completed=True)

    def test_task_list_view(self):
        # Test if the task list view returns a status code of 200
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

        # Test if the rendered HTML contains task titles
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_task_detail_view(self):
        # Test if the task detail view for a specific task returns a status code of 200
        task = Task.objects.get(title="Task 1")
        response = self.client.get(reverse('task_detail', args=(task.id,)))
        self.assertEqual(response.status_code, 200)

        # Test if the rendered HTML contains the task title
        self.assertContains(response, "Task 1")

    def test_task_completion(self):
        # Test if a task can be marked as completed
        task = Task.objects.get(title="Task 1")
        task.completed = True
        task.save()

        # Test if the task is now marked as completed
        updated_task = Task.objects.get(title="Task 1")
        self.assertTrue(updated_task.completed)

    def test_task_creation(self):
        # Test if a new task can be created
        new_task_data = {
            'title': 'New Task',
            'completed': False,
        }
        response = self.client.post(reverse('task_create'), data=new_task_data)

        # Test if the task was successfully created
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Test if the new task is in the database
        new_task = Task.objects.get(title="New Task")
        self.assertIsNotNone(new_task)
