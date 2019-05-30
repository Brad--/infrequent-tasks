"""Packaging settings"""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from infrequent_tasks import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

class RunTests(Command):
    """Run all tests"""
    description = 'Run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test'])
        raise SystemExit(errno)


setup(
    name = 'infrequent_tasks',
    version = __version__,
    description = 'A command line util to keep track of tasks I don\'t need to do very often, like dusting the top of my ceiling fans',
    long_description = long_description,
    url = 'https://github.com/Brad--/infrequent-tasks-cli',
    author = 'Brad Smith',
    author_email = 'nothanks@gmail.com',
    license = 'UNLICENSED',
    classifiers = [
        'Intended Audience :: People who like todo lists',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating Systems :: OS Independent',
        'Programming Language :: Python 3.7'
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'appdirs', 'python-dateutil'],
    extras_require = {
        'test': ['pytest']
    },
    entry_points = {
        'console_scripts': [
            'infrequent_tasks=infrequent_tasks.cli:main'
        ]
    },
    cmdClass = {'test': RunTests}
)