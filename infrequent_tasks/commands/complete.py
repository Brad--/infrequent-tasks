"""Mark a task as complete"""

from .base_command import BaseCommand

class CompleteCommand(BaseCommand):
    """Mark a task as complete"""

    def run(self):
        print(self.options)
        self.markTaskComplete()

    def markTaskComplete(self):
        try:
            target_task = int(self.options['<task-number>'])
            task_list = self.storage_client.readTaskList()

            if target_task > len(task_list) or target_task <= 0:
                self.printInvalidTaskNumberMessage(target_task)
            
            task_list[target_task - 1].markComplete()
            print('Task "' + task_list[target_task - 1].name + '" marked as complete!')
        except ValueError as e:
            print(e)


    def printInvalidTaskNumberMessage(self, task_number):
        print ('Invalid <task-number> given: ' + str(task_number))