"""
The setup.py file is a script used to configure the package for installation. It includes metadata such as the name, version, author, description, required packages, and classifiers for the Python Package Index (PyPI). In this case, it's setting up a project named 'tokeniser', authored by Eugene Evstafev.
"""

from setuptools import setup, find_packages

setup(
    name="tokeniser",
    version="0.0.3",
    author="Eugene Evstafev",
    author_email="chigwel@gmail.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chigwell/tokeniser",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
