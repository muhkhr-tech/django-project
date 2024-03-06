#type:ignore

from django.test import TestCase
from django.urls import reverse

from ..models import Todo

class TodoModel(TestCase):
    def test_no_todos(self):
        new_todo = Todo()
        new_todo.title = 'Belajar ...'
        new_todo.status = 'DOoing'
        new_todo.save()

