# -*- coding: utf-8 -*-
import io
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup

from tox_test_command import ToxTestCommand
from sphinx.setup_command import BuildDoc
from version_extractor import extract_version_init


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


setup(
    name='dice-notation',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=extract_version_init(_source_package),
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
        'Topic :: Games/Entertainment :: Role-Playing'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'antlr4-python3-runtime',
        'bernardomg.tox-test-command',
        'bernardomg.version-extractor'
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={
        'build_docs': BuildDoc,
        'test': ToxTestCommand
    },
    python_requires='>=3.6',
)
