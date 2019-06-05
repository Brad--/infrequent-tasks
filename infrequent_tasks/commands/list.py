# list.py
"""The list command"""

from .base_command import BaseCommand
from infrequent_tasks.util import StorageClient

import logging

class ListCommand(BaseCommand):
    """Lists tasks and their associated data"""

    def run(self):
        logging.debug('ListCommand options: ')
        logging.debug(self.options)
        ListCommand.printList(self.storage_client.getAllTasks(), self.options['todo'])

    # TODO This should print a better, more tightly columned list. Right now it just dumps what the output file will be, basically
    #   Should print line numbers too, so you can mark completed by line number
    @staticmethod
    def printList(task_list, todo):
        if len(task_list) == 0:
            ListCommand.printEmptyListMessage()
        else:
            if todo:
                for task in task_list:
                    if not task.complete:
                        task.print()
            else:
                print('\t'.join(['Name', 'Repeat', 'Completed', 'Last Completion']))
                for task in task_list:
                    task.print()
    
    @staticmethod
    def printEmptyListMessage():
        print('You don\'t have any tasks!')
        print('You can create one by running: `infrequent_tasks new`')