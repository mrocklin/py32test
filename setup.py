import os
from setuptools import setup, find_packages
import sys

if sys.version_info[0] == 2:
    from Cython.Build import cythonize
    kwargs = {'ext_modules': cythonize(os.path.join("py32test", "*.py"),
                                       language_level='3')}
else:
    kwargs = {}

setup(
    name='py32test',
    version='1.0.0',
    packages=find_packages(),
    **kwargs
)

