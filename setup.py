'''
This setup.py file is used to set up the 'tokeniser' package. It specifies various metadata such as the author, version, and required dependencies.
The 'setuptools' library is used to facilitate the packaging and distribution of this Python package.
The package is configured to be installed from source code on GitHub using pip. The necessary packages are discovered automatically and specified for installation. Classifiers are used to categorize the project according to aspects such as license, development status, intended audience, programming language, and operating system compatibility.
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