#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-intercom',
      version='0.0.2',
      description='Singer.io tap for extracting data from the Intercom API',
      author='jeff.huth@bytecode.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_intercom'],
      install_requires=[
          'backoff==1.8.0',
          'requests==2.22.0',
          'singer-python==5.8.1'
      ],
      entry_points='''
          [console_scripts]
          tap-intercom=tap_intercom:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_intercom': [
              'schemas/*.json',
              'tests/*.py'
          ]
      })
