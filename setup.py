#!/usr/bin/env python3

from setuptools import setup

config = {
    'version': '1.0.0',
    'name': 'BAGELp',
    'description': 'This is parallel implementation of original BAGEL algorithm',
    'author': 'Shriram Bhosle',
    'url': 'https://github.com/sb43/BAGELp',
    'author_email': 'sb43@sanger.ac.uk',
    'python_requires': '>= 3.3',
    'setup_requires': ['pytest','pytest-cover', 'radon'],
    'install_requires': ['scipy', 'numpy', 'tzlocal'],
    'packages': ['BAGELp'],
    'package_data': {'BAGELp':['config/*.conf','parallel/*.py']},
    'entry_points': {
        'console_scripts': ['BAGELp=BAGELp.command:main'],
    }
}

setup(**config)
