#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : setup.py
# @Author: hanyan_news
# @Desc  :


from distutils.core import setup
from setuptools import find_packages


with open("README.rst", "r") as f:
  long_description = f.read()


setup(name='dnspod_domain_log',  # 包名
      version='1.0.5',  # 版本号
      description='return the log for dns resolution',
      long_description=long_description,
      author='hanyan_news',
      author_email='hanyan0572@gmail.com',
      url='https://github.com/hanyan007/DNSPOD_Domain_Log.git',
      project_urls={  # Optional
          "Source": 'https://github.com/hanyan007/DNSPOD_Domain_Log.git',
      },
      install_requires=["package-tea-hanyan==1.0.3", "package-tea-seven==1.0.0", "package-tea-six==1.0.0"],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
