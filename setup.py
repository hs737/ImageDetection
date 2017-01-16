import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Image Detection',
    version='0.0.1',
    description=('A module that can be imported and used via the command line '
                 'to query for images with specific attributes in '
                 'a file system.'),
    license='BSD',
    keywords='image duplicate search detection',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Multimedia",
        "Topic :: Utilities"
    ],
    packages=['imagedetection', 'tests'],
    install_requires=[
        'click',
        'future',
        'scipy',
        'numpy',
        'pillow',
        'imagehash',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
            'imagedetection = imagedetection.imagesearch_commandline:cli'
        ]
    }
)
