# -*- coding: utf-8 -*-

"""
setup.py
"""

from setuptools import setup
from setuptools import find_packages

dist = setup(
    name='alison',
    version='0.0.1',
    author='Jonatan Zafar',
    author_email='jonatanzafar59@gmail.com',
    description='DNS over TLS proxy',
    packages=find_packages(),
    install_requires=[
        'argparse',
        'prometheus_client',
        'dnspython',
        'tornado',
        'healthcheck',
        'flask',
        'gevent'
    ],
    python_requires='>=3.4, <4',
    classifiers=[
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'alison = alison.main:main',
        ],
    }
)
