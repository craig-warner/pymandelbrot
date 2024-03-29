#!/usr/bin/env python3
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymandelbrot", 
    version="1.0.0",
    author="Craig Warner",
    author_email="cgwarner2012@gmail.com",
    description="Mandelbrot Drawer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craig-warner/pymandelbrot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/pymandelbrot'],
)
