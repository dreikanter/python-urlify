# coding: utf-8

import os
from setuptools import setup
import urlify


setup(
    name='urlify',
    description='This library provides Django\'s urlify.js ' \
                'functionality ported to Python.',
    version=urlify.__version__,
    license=urlify.__license__,
    author=urlify.__author__,
    url=urlify.__url__,
    py_modules=['urlify'],
    platforms=['any'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
       'Development Status :: 5 - Production/Stable',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: MIT License',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3.3',
    ],
)
