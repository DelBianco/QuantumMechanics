# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='qmworld',
    version='0.0.1',
    description='Quantum Mechanics Study',
    long_description=readme,
    author='André Del Bianco Giuffrida',
    author_email='andredbg@gmail.com',
    url='https://github.com/DelBianco/QuantumMechanics',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

