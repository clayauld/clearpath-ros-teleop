#! /usr/bin/python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    #packages=['teleop'],
    scripts=['scripts/teleop.py']
    #package_dir={'': 'src'}
)

setup(**d)
