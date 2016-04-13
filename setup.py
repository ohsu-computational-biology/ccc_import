#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "docopt>=0.6.2",
    "elasticsearch>=2.3.0",
    "python-dateutil>=2.5.0",
    "pytz>=2015.7",
    "requests>=2.9.1",
    "six>=1.10.0",
    "tsv>=1.1",
    "urllib3>=1.14"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ccc_import',
    version='0.1.0',
    description="Command line tool for importing/registering resources with CCC.",
    long_description=readme,
    author="Ben Bimber",
    author_email='bimber@ohsu.edu',
    url='https://github.com/ohsu-computational-biology/ccc_import',
    packages=[
        'ccc_import',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='ccc_import',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    scripts=['bin/ccc_import'],
    test_suite='test',
    tests_require=test_requirements,
    dependency_links = [
        #TODO: this should only be temporary until we have a better location for the module
        'https://github.com/ohsu-computational-biology/ccc_client/tarball/master'
    ]
)