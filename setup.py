# coding: utf-8
from setuptools import setup, find_packages
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


__version__ = "0.0.1"

setup(
    name='demeter',
    version=__version__,
    keywords='demeter',
    description=u'data centor',
    long_description=read("README.md"),

    url='https://github.com/guoxuequan/demeter',
    author='guoxueuan',
    author_email='guoxuequan@gmail.com',

    packages=find_packages(),
    package_data={
        "demeter": ["*.json"],
    },
    install_requires=read("requirements.txt").splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'],
)
