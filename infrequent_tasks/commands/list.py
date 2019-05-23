# list.py
"""The list command"""

from .base_command import BaseCommand
from infrequent_tasks.util import StorageClient

class ListCommand(BaseCommand):
    """Lists tasks and their associated data"""

    def __init__(self, options, *args, **kwargs):
        super().__init__(options, *args, **kwargs)

        self.storage_client = StorageClient()

    def run(self):
        print('options: ')
        print(self.options)
        self.printList()

    def printList(self):
        task_list = self.storage_client.getTaskList()
        if len(task_list) == 0:
            self.printEmptyListMessage()
        else:
            if self.options['todo']:
                for task in task_list:
                    if not task.complete:
                        task.print()
            else:
                for task in task_list:
                    task.print()
    
    def printEmptyListMessage(self):
        print('You don\'t have any tasks!')
        print('You can create one by running: `infrequent_tasks new`')