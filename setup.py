import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Image Search',
    version='0.0.1',
    description=('A module that can be imported and used via the command line '
                 'to query for images with specific attributes in '
                 'a file system.'),
    license='BSD',
    keywords='image duplicate search detection',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ],
    packages=['imagedetection', 'tests'],
    install_requires=[
        'click',
        'scipy',
        'numpy',
        'pillow',
        'imagehash',
    ],
    entry_points={
        'console_scripts': [
            'imagedetection = imagedetection.imagesearch_commandline:cli'
        ]
    }
)
