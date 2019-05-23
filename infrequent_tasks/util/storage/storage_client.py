"""Read and write AppData"""

from appdirs import user_data_dir

from infrequent_tasks.models import TaskModel

import os.path
from os.path import abspath, dirname, join
import pathlib

class StorageClient():
    """Read and Write AppData"""

    def __init__(self):
        self.app_name = 'InfrequentTasks'
        self.app_author = 'BradsStuff'
        self.task_filename = 'user_tasks.txt'
        self.app_data_path = user_data_dir(self.app_name, self.app_author)

    #Task list folder file should be as follows (tab separated):
    #Name   RepeatFrequency     Complete    LastCompletion
    def getTaskList(self):
        try:
            tasks = []
            path_to_tasks = join(self.app_data_path, self.task_filename)
            with open(path_to_tasks) as task_file:
                lines = task_file.readlines()
                for line in lines:
                    task_model = TaskModel()
                    task_model.deserialize(line)
                    tasks.append(task_model)
            return tasks
        except IOError:
            pathlib.Path(self.app_data_path).mkdir(parents = True, exist_ok = True)
            return []