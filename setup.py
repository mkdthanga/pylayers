#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for pylayers 
"""
import numpy

from setuptools import setup,find_packages

setup(name='pylayers' ,
      version='0.1',
      description='Python LocAlization mobilitY Electromagnetic Radio Simulator',
      author='AMIOT Nicolas,UGUEN Bernard and LAARAIEDH Mohamed',
      author_email='nicolas.amiot@univ-rennes1.fr, bernard.uguen@univ-rennes1.fr, mohamed.laaraeidh@univ-rennes1.fr',
      url='https://github.com/niamiot/RGPA',
      include_dirs = [numpy.get_include()],
#      install_requires=[
#        'numpy>=1.6.1',
#        'scipy>=0.10.1',
#        'networkx>=1.6',
#        'matplotlib>=1.1.0',
#        'SimPy>=2.2'
#                        ],
      packages=find_packages()
)


