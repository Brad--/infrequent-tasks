"""Add a new task. Should allow it to be created as already complete!"""

from .base_command import BaseCommand
from infrequent_tasks.util import StorageClient
from infrequent_tasks.models import TaskModel
from infrequent_tasks.commands import ListCommand

class NewCommand(BaseCommand):
    """Create a new task"""

    def run(self):
        print(self.options)
        self.guidedTaskCreate()

    def guidedTaskCreate(self):
        name = self.getNameInput()
        repeat_frequency = self.getRepeatFrequencyInput()
        complete = self.getCompleteInput()
        self.saveNewTask(name, repeat_frequency, complete)

    def getNameInput(self):
        name = input("Enter a name for your new task: ")
        while '\t' in name:
            name = input("Enter a name for your new task (no tabs!): ")
        return name

    def getRepeatFrequencyInput(self):
        while True:
            repeat_frequency = input("How often does the task repeat? (enter #d, #m, #y, ie 123d, 2m): ")

            # if this fails to cast to int, it's invalid 
            try:
                int(repeat_frequency[:len(repeat_frequency) - 1])
            except ValueError:
                continue
                
            repeat_unit = repeat_frequency[len(repeat_frequency) - 1:]
            if repeat_unit not in ['d', 'm', 'y']:
                continue
            
            return repeat_frequency

    def getCompleteInput(self):
        yesInputs = ['yes', 'y', 'yup', 'yeah']
        noInputs = ['no', 'n', 'nah']
        while True:
            complete = input('Do you want this task to start marked as Complete? (Y/N): ')
            if complete in yesInputs:
                return True
            elif complete in noInputs:
                return False
            else:
                continue

    def saveNewTask(self, name, repeat_frequency, complete):
        task_model = TaskModel()
        task_model.createNewTask(name, repeat_frequency, complete)

        task_list = self.storage_client.readTaskList()
        task_model.id_ = task_list[len(task_list) - 1].id_
        task_list.append(task_model)

        print('Successfully added "' + task_model.name + '" to your tasks list:')
        ListCommand.printList(task_list, False)

        self.storage_client.writeTaskList(task_list)
