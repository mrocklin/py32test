from setuptools import setup, find_packages
import os
from Cython.Build import cythonize

setup(
    name='py32test',
    version='0.0.1',
    ext_modules = cythonize(os.path.join("py32test", "*.py"),
                            language_level='3'),
    packages=find_packages(),
)

