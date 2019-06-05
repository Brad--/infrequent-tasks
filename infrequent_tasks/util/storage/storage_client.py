"""Read and write AppData"""

from appdirs import user_data_dir
from infrequent_tasks.models import TaskModel
from os.path import abspath, dirname, join

import atexit
import pathlib
import logging

class StorageClient():
    """Read and Write AppData"""

    def __init__(self):
        self.app_name = 'InfrequentTasks'
        self.app_author = 'BradsStuff'
        self.task_filename = 'user_tasks.txt'
        self.app_data_path = user_data_dir(self.app_name, self.app_author)
        self.task_filepath = join(self.app_data_path, self.task_filename)

        self.tasks = self._readTaskList()

        atexit.register(self._exit)

    def _exit(self):
        self._writeTaskList()

    #Task list folder file should be as follows (tab separated):
    #Name   RepeatFrequency     Complete    LastCompletion
    def _readTaskList(self):
        try:
            tasks = []
            with open(self.task_filepath) as task_file:
                lines = task_file.readlines()
                for i, line in enumerate(lines):
                    task_model = TaskModel()
                    # id is line number
                    task_model.deserialize(i + 1, line)
                    tasks.append(task_model)
            return tasks
        except IOError:
            logging.info('Error reading AppData, creating AppData directory')
            pathlib.Path(self.app_data_path).mkdir(parents = True, exist_ok = True)
            return []

    def _writeTaskList(self, tasks):
        # Overwrite task file with given tasks
        try:
            with open(self.task_filepath, 'w') as task_file:
                for task in tasks:
                    task_file.write(task.getSerializedString() + '\n')
        except IOError as e:
            logging.error('Error writing tasks to file: ')
            logging.error(e)
            raise e

    def getAllTasks(self):
        return self.tasks

    def getTaskById(self, id):
        return [task for task in self.tasks if task.id is id][0]

    def addTask(self, task):
        task.id_ = self.tasks[len(self.tasks) - 1].id_
        self.tasks.append(task)