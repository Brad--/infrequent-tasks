# list.py
"""The list command"""

from .base_command import BaseCommand

class ListCommand(BaseCommand):
    """Lists tasks and their associated data"""

    def run(self):
        print('options:')
        print(self.options)