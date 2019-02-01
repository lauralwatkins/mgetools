#!/usr/bin/env python

from setuptools import setup

setup(
    name="mgetools",
    version="0.0",
    description="A collection of python functions to calculate various "\
        +"quantities and perform various tasks for Multi-Gaussian Expansions "\
        +"(MGEs).",
    author="Laura L Watkins",
    author_email="lauralwatkins@gmail.com",
    url="https://github.com/lauralwatkins/mgetools",
    package_dir = {
        "mgetools": "mgetools",
    },
    packages=["mgetools"],
)
