#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-
import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="meu-projeto-google",
    license="Apache License 2.0",
    version='0.1.0',
    author='Felipe Lima Vieira',
    author_email='felipe.acbb@gmail.com',
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="Projeto usando Google SDK",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=[
        "google-adk"
        "pandas",
        "pandasql",
        "matplotlib",
        "streamlit",
        "openpyxl"
    ],
)