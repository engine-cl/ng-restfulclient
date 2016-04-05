#!/usr/bin/env python
__copyright__ = "Copyright (C) 2016 eNgine.cl"
__revision__ = "$Revision$"
__license__ = "BSD License"
__version__ = "$Version$"
__author__ = "Jorge A. Medina"
__date__ = "12/3/16"
import os
from distutils.core import setup
try:
    from setup_tools import find_packages
except ImportError:
    def find_packages():
        """When setup_tools find_packages fail because are not installed or some similar behavior
        this overwrite it and return default package.
        :return: list
        """
        return ['restfulclient']


def read(f):
    """ Read a file and get string from it
    :param f: file to read
    :return: file content as string
    """
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(
    name="restfulclient",
    version="0.1",
    description="async RESTful client in python",
    author="Jorge A. Medina",
    platforms=["Unix"],
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "aiohttp==0.21.5",
        "chardet=2.3.0",
        "cchardet==1.0.0",
        "ng_factory"
    ]
)