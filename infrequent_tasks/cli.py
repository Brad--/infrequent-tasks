"""Infrequent Tasks - A CLI to manage things like replacing the filter on the AC unit

Usage:
    infrequent_tasks list
    infrequent_tasks list todo
    infrequent_tasks complete <task-number>
    infrequent_tasks new
    infrequent_tasks delete <task-number>

Options:
    -h --help   Show this screen.
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
            print(module)
            infrequent_tasks.commands = getmembers(module, isclass)
            print(infrequent_tasks.commands)
            print (getmembers(module, isclass))
            # Parse commands by class name, returning only the Class (runnableCommands[1]) and return the first item in the list (should only be one)
            command = [runnableCommands[1] for runnableCommands in infrequent_tasks.commands if commandMatchesKey(runnableCommands, key)][0]
            command = command(arguments)
            command.run()

def commandMatchesKey(runnableCommands, key):
    return runnableCommands[0] != 'BaseCommand' and key.upper() in runnableCommands[0].upper()