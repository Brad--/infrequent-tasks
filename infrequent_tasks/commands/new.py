"""Add a new task. Should allow it to be created as already complete!"""

from .base_command import BaseCommand

class NewCommand(BaseCommand):
    """Create a new task"""

    def run(self):
        print('Hi I\'m new')