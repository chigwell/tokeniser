'''
This is a setup script for a Python package named 'tokeniser'. The script provides information about the package, such as its name, version, author, description, long description, URL, packages to include, installation requirements, classifiers, and Python version requirement.
'''


from setuptools import setup, find_packages

setup(
    name='tokeniser',
    version='0.0.3',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/tokeniser',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)