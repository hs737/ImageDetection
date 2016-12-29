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
    # description=('A module that can be imported and used via the command line '
    #              'to query for images with specific attributes in '
    #              'a file system.'),
    # license='MIT',
    # keywords='image duplicate search detection',
    # long_description=read('README.md'),
    # classifiers=[
    #     "Development Status :: 2 - Pre-Alpha",
    #     "Environment :: Console",
    #     "License :: OSI Approved :: MIT License",
    #     "Natural Language :: English"
    # ],
    # # package_dir = {'': 'imagedetection'},
    # py_modules=['imagedetection'],
    # # packages=['imagedetection', 'imagedetection.index', 'tests'],
    # # packages=find_packages(),
    packages=['imagesearch', 'tests'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'imagesearch = imagesearch.__main__:main'
        ]
    },
    # # entry_points='''
    # #     [console_scripts]
    # #     callimagedetection=imagedetection.index:cli
    # # ''',
)
