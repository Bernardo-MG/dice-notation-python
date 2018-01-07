# -*- coding: utf-8 -*-
import ast
import re
import io
from os.path import dirname
from os.path import join
from codecs import open

from setuptools import find_packages, setup
from bernardomg.tox_test_command import ToxTestCommand

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Source package
_source_package = 'dice_notation/'

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# Gets the version for the source folder __init__.py file
def read_version(path):
    # Regular expression for the version
    _version_re = re.compile(r'__version__\s+=\s+(.*)')

    with open(path + '__init__.py', 'rb', encoding='utf-8') as f:
        version_lib = f.read()
        version_lib = _version_re.search(version_lib).group(1)
        version_lib = str(ast.literal_eval(version_lib.rstrip()))

    return version_lib

setup(
    name='dice-notation',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=read_version(_source_package),
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
        'test': ToxTestCommand
    },
)
