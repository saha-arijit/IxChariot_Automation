#!/usr/bin/python

import os
import sys
from setuptools import setup, find_packages

# Must be ran as root or as sudo
if os.getuid() != 0:
    print('ERROR: Need to run as root')
    sys.exit(1)

# Generate the requirements from the file for old instructions
print('INFO: Generating the requirements from requirements.txt')
packages = []
for line in open('requirements.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

# Run setuptools for pip
setup(
    name='IxChariot',
    author='ECI Networks',
    install_requires=packages,
    packages=find_packages(),
)
