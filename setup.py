# -*- coding: utf-8 -*-
import ast
import re
import sys
import io
from os.path import dirname
from os.path import join
from codecs import open

from setuptools import find_packages, setup
from setuptools.command.test import test as test_command
from distutils.command.clean import clean as clean_command
from distutils.cmd import Command

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Source package
_source_package = 'dice_notation'

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# Gets the version for the source folder __init__.py file
with open(_source_package + '/__init__.py', 'rb', encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))


class _ToxTester(test_command):
    """
    Tox test command.

    Calls tox for running the tests.
    """
    user_options = [
        ('test-module=', 'm', "Run 'test_suite' in specified module"),
        ('test-suite=', 's',
         "Run single test, case or suite (e.g. 'module.test_suite')"),
        ('test-runner=', 'r', "Test runner to use"),
        ('profile=', 'p', 'Test profile to use')
    ]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.profile = None

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []

        if self.profile is not None:
            # Adds the profile argument
            # For example: '-e=py36'
            self.test_args.append('-e=' + self.profile)

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox

        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


class _RequirementsCommand(Command):
    """
    Requirements command.

    Installs all the requirements defined in the requirements file with pip.
    """
    description = 'install the requirements defined in requirements.txt'
    user_options = [('requirements-file=', 'f', 'requirements file to use')]

    def initialize_options(self):
        self.requirements_file = None

    def finalize_options(self):
        if self.requirements_file is None:
            self.requirements_file = 'requirements.txt'

    def run(self):
        # import here, cause outside the eggs aren't loaded
        import pip

        with open(self.requirements_file) as file:
            requirements = file.read().splitlines()

        # Removes empty lines
        requirements = filter(lambda k: bool(k.strip()), requirements)
        # Removes comments
        requirements = filter(lambda k: not k.strip().startswith('#'), requirements)

        # Installs the requirements
        for requirement in requirements:
            pip.main(['install', requirement])

setup(
    name='dice-notation',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=version_lib,
    description='Dice notation tools',
    author='Bernardo Martínez Garrido',
    author_email='programming@bernardomg.com',
    license='MIT',
    url='https://github.com/Bernardo-MG/dice-notation-python',
    download_url='https://pypi.python.org/pypi/dice-notation',
    keywords=['dice', 'dice notation', 'rpg', 'parser'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment :: Role-Playing'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'ply'
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={
        'test': _ToxTester,
        'requirements': _RequirementsCommand
    },
)
