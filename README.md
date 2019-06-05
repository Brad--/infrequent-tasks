# Infrequent-tasks 
A CLI to manage things like replacing the filter on the AC unit and dusting the top of my ceiling fan

# Using the app
```
Usage:
    infrequent_tasks list
    infrequent_tasks list todo
    infrequent_tasks mark (complete | todo) <task-number>
    infrequent_tasks new
    infrequent_tasks delete <task-number>

    infrequent_tasks dump <output-filepath>
    infrequent_tasks load <input-filepath>

Options:
    -h --help   Show this screen
```

# Installing
*This project is built with python3.x!*

To install library dependencies, run:
`$ pip install -e .[test]`