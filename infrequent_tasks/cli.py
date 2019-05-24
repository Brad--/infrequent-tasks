"""Infrequent Tasks - A CLI to manage things like replacing the filter on the AC unit

Usage:
    infrequent_tasks list
    infrequent_tasks list todo
    infrequent_tasks mark complete <task-number>
    infrequent_tasks mark todo <task-number>
    infrequent_tasks new
    infrequent_tasks delete <task-number>

    infrequent_tasks dump <output-filepath>
    infrequent_tasks load <input-filepath>

Options:
    -h --help   Show this screen
"""

from inspect import getmembers, isclass
from os.path import join

from appdirs import user_log_dir
from docopt import docopt

import pathlib
import logging

from __init__ import __version__

def main():
    """CLI Entrypoint"""
    import infrequent_tasks.commands
    arguments = docopt(__doc__, version = __version__)
    setupLogger(arguments)

    for (key, value) in arguments.items():
        if hasattr(infrequent_tasks.commands, key) and value:
            module = getattr(infrequent_tasks.commands, key)
            infrequent_tasks.commands = getmembers(module, isclass)
            # Parse commands by class name, returning only the Class (runnableCommands[1]) and return the first item in the list (should only be one)
            command = [runnableCommands[1] for runnableCommands in infrequent_tasks.commands if commandMatchesKey(runnableCommands, key)][0]
            command = command(arguments)
            command.run()

def setupLogger(arguments):
    log_level = logging.DEBUG
    app_name = 'InfrequentTasks'
    app_author = 'BradsStuff'
    log_dir = user_log_dir(app_name, app_author)
    logfile_path = join(log_dir, 'infrequent-tasks-cli.log')
    pathlib.Path(log_dir).mkdir(parents = True, exist_ok = True)
    
    logging.basicConfig(
        filename=logfile_path, 
        level=log_level
        )
    logging.info('Testing 1 2 3')

def commandMatchesKey(runnableCommands, key):
    return runnableCommands[0] != 'BaseCommand' and key.upper() in runnableCommands[0].upper()