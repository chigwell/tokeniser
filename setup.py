"""
This Python script sets up a package named 'tokeniser' with version '0.0.3'. The author is Eugene Evstafev, and the description, long_description, and other metadata are defined here.
The package requires certain packages to be installed which are listed in the install_requires section. Classifiers are used to categorize and organize software packages into specific groups based on their functionality and intended audience.
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
