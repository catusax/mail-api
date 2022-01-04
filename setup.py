# -*- coding: utf-8 -*-
# Author: coolrc <root@coolrc.me>
# date:   2021/7/12
"""Setup script of mail-api"""

import os
from setuptools import setup, find_packages

setup(
    name="mail-api",
    version="0.0.1",
    author="coolrc",
    author_email="root@coolrc.me",
    description="Simply send email using http request.",
    license="GPLv3",
    url="https://github.com/coolrc136/mail-api",
    # packages=['an_example_pypi_project', 'tests'],
    long_description=__doc__,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "Flask",
        "validit[yaml]==1.3.2"
    ]
)
