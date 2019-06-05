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
        # tasks = self.storage_client.getTaskById()
        # Get task by ID? Yeah I'm gonna go do that
        print('mark complete')

    def markTodo(self, task_number):
        print('mark todo')