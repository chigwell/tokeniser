'''
This setup.py file is used to configure and package the 'tokeniser' project for distribution.
The script specifies metadata such as the name, version, author, description, long_description, URL, packages, install requirements, classifiers, and the Python version required.
It also uses the find_packages() function to automatically discover all the necessary packages.
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