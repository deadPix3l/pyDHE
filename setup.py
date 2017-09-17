#!/usr/bin/env python

from setuptools import setup

longdesc ="""
pyDHE
============

pyDHE is a simple to use Diffie-Hellman implementation written in python, for
python. It makes using Diffie-Hellman a breeze so you can focus on the real
crypto.

This library was created out of need, because none of the standard crypto
libraries provide DHE, and of the separate libraries out there, they were
all complicated, incomplete, or requireed manual installation from github.
This library is to change that. The goal is too provide a simple API that is
similar to the pyCrypto and pyCryptodome libraries. The goal is familiarity
and seamless blending with existing code.
"""

setup(
    name='pyDHE',
    #packages=['scanless', 'scanless.cli', 'scanless.scanners'],
    version='1.0.0',
    description='a fully python Diffie Hellman implementation',
    long_description = longdesc,
    license='BSD',
    url='https://github.com/deadPix3l/pyDHE',
    author='Skyler Curtis',
    author_email='skylerr.curtis@gmail.com',

    install_requires = ['Crypto'],
    packages =  ["pyDHE"],
    package_dir = { "pyDHE": "lib/pyDHE"},
    platforms = 'Posix; MacOS X; Windows',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Security :: Cryptography',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
