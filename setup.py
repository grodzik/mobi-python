#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

VERSION = '0.0.1'

setup(name='mobi',
      version=VERSION,
      description='Mobi Python Library',
      author='Elliot Kroo',
      url='https://github.com/kroo/mobi-python',
      license='MIT',
      packages=['mobi'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Internet',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4'
      ],
      download_url = 'https://github.com/grodzik/mobi-python/tarball/'+VERSION,
     )
