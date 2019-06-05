"""Mark a task as todo or complete"""

from .base_command import BaseCommand
from infrequent_tasks.util import StorageClient
from infrequent_tasks.commands import ListCommand

import logging

class MarkCommand(BaseCommand):
    """Mark a task as todo or complete"""

    def run(self):
        task_number = self.options['<task-number>']
        if self.options['complete']:
            self.markComplete(task_number)
        if self.options['todo']:
            self.markComplete(task_number)
            

    def markComplete(self, task_number):
        task = self.storage_client.getTaskById(task_number)
        if task.complete:
            print('That task is already complete!')
        else:
            task.markComplete()

    def markTodo(self, task_number):
        task = self.storage_client.getTaskById(task_number)
        if not task.complete:
            print('That task is already marked as todo!')
        else:
            task.markTodo()