# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

from pantulipy import (__version__, __author__, __package__, __email__, __license__, __description__, __dependencies__,
                       __keywords__)

setup(
    name=__package__,
    version=__version__,
    packages=find_packages(
        exclude=['.idea*', 'build*', '{}.egg-info*'.format(__package__), 'dist*', 'venv*']),
    url='https://github.com/havocesp/{}'.format(__package__),
    license=__license__,
    packages_dir={'': __package__},
    keywords=__keywords__,
    author=__author__,
    author_email=__email__,
    long_description=__description__,
    description=__description__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=__dependencies__
)
