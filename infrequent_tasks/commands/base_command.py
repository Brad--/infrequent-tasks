"""The base class for commands"""

class BaseCommand(object):
    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('Extending classes need to implement run()')