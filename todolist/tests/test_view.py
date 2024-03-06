#type:ignore

from django.test import TestCase
from django.urls import reverse

from ..models import Todo

def create_a_todo():
    new_todo = Todo()
    new_todo.title = 'Belajar ...'
    new_todo.status = 'DO'
    new_todo.save()

class TodoIndexView(TestCase):
    def test_no_todos(self):
        response = self.client.get(reverse("todos:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No todos are available")
        self.assertQuerySetEqual(response.context["latest_todo_list"], [])

    def test_todo_list(self):
        create_a_todo()
        response = self.client.get(reverse("todos:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Form Add Todo</h1>")

