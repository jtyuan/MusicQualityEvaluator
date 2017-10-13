#!/usr/bin/env python

from distutils.core import setup

setup(name='Music Quality Evaluator',
      version='0.1',
      description='Music Quality Evaluator is tool to evaluate the quality of computer generated music pieces.',
      author='Tianyuan Jiang',
      author_email='tianyuaj@andrew.cmu.edu',
      packages=['music_eval', 'music_eval.evaluators']
     )
