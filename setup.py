#!/usr/bin/env python3
"""
Happy Frog - Educational HID Emulation Framework
Setup script for production package installation
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "Educational HID emulation framework for cybersecurity learning"

setup(
    name="happy_frog",
    version="0.2.6",
    author="ZeroDumb",
    author_email="zero@zerodumb.dev",
    description="Educational HID emulation framework for cybersecurity learning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZeroDumb/happy-frog",
    packages=find_packages(),
    py_modules=["main", "ducky_converter"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Education",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware",
        "Topic :: System :: Emulators",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
        "colorama>=0.4.4",
    ],
    entry_points={
        "console_scripts": [
            "happy-frog=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "happy_frog_parser": ["*.py"],
        "devices": ["*.py"],
        "payloads": ["*.txt"],
    },
    keywords="cybersecurity, education, hid, ducky, microcontroller, circuitpython, automation, scripting, educational, ethical, open source, free, gplv3, froggy basher, happy frog",
    project_urls={
        "Bug Reports": "https://github.com/ZeroDumb/happy-frog/issues",
        "Source": "https://github.com/ZeroDumb/happy-frog",
        "Documentation": "https://github.com/ZeroDumb/happy-frog/tree/main/docs",
        "Homepage": "https://zerodumb.dev",
    },
    license="GNU General Public License v3",
    license_files=("LICENSE",),
) 
