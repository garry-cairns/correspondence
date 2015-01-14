#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import correspondence
version = correspondence.__version__

setup(
    name='Correspondence',
    version=version,
    author='',
    author_email='garryjcairns@gmail.com',
    packages=[
        'correspondence',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['correspondence/manage.py'],
)
