"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the dabs_python_example project.
"""

import os

from setuptools import setup

local_version = os.getenv("LOCAL_VERSION")
version = "0.0.1"

setup(
    version=f"{version}+{local_version}" if local_version else version,
)
