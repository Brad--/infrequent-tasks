"""Infrequent Tasks - A CLI to manage things like replacing the filter on the AC unit

Usage:
    infrequent_tasks list
    infrequent_tasks list todo [--within-days n | -w n]
    infrequent_tasks complete <task-number>
    infrequent_tasks new <date> [--complete | -c]

Options:
    -h --help   Show this screen.
    -w --within-days   List items are going to be in the todo state within n days
    -c --complete
"""

from inspect import getmembers, isclass

from docopt import docopt

from __init__ import __version__

def main():
    """CLI Entrypoint"""
    import infrequent_tasks.commands
    arguments = docopt(__doc__, version = __version__)

    for (key, value) in arguments.items():
        if hasattr(infrequent_tasks.commands, key) and value:
            module = getattr(infrequent_tasks.commands, key)
            infrequent_tasks.commands = getmembers(module, isclass)
            command = [runnableCommands[1] for runnableCommands in infrequent_tasks.commands if runnableCommands[0] != 'BaseCommand'][0]
            command = command(arguments)
            command.run()