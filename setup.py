#!/usr/bin/env python3
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

NAME = "numpyGL"
version = "0.1"

setup(
    name = NAME,
    version = version,
    packages = find_packages('src', exclude='dev'),
    package_dir = {'': 'src'},
    install_requires=['numpy', 'vispy'],
    author = "Laurent Perrinet INT - CNRS",
    author_email = "Laurent.Perrinet@univ-amu.fr",
    description = "numpyGL. A simple framework to display numpy array on a screen. And only that.",
    long_description=open("README.md").read(),
    license = "GPLv2",
    keywords = ('computational neuroscience', 'simulation', 'visualization', 'computer vision', 'psychophysics'),
    url = 'https://github.com/meduz/' + NAME, # use the URL to the github repo
    download_url = 'https://github.com/meduz/' + NAME + '/tarball/' + version,
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License'
                   'Operating System :: POSIX',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                  ],
     )

