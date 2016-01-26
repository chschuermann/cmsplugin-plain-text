#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import cmsplugin_plain_text

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = cmsplugin_plain_text.__version__

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='cmsplugin-plain-text',
    version=version,
    description="""A simple plaintext plugin for django CMS.""",
    long_description=readme + '\n\n' + history,
    author='Christian Schürmann',
    author_email='christian.schuermann@bluewin.ch',
    url='https://github.com/chschuermann/cmsplugin-plain-text',
    packages=[
        'cmsplugin_plain_text',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='cmsplugin-plain-text',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',        
    ],
)
