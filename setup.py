
# !/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='unit',
    version='0.1',
    description='Create Systemd unit files with love',
    author='CODEBASE PK',
    packages=find_packages(),
    scripts=['main']
)
