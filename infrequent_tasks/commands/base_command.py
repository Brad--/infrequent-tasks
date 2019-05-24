"""The base class for commands"""

from infrequent_tasks.util import StorageClient

class BaseCommand(object):
    def __init__(self, options, *args, **kwargs):
        self.storage_client = StorageClient()
        
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('Extending classes need to implement run()')