from distutils.core import setup
import os
from Cython.Build import cythonize

setup(
    name='myproj',
    version='0.0.1',
    ext_modules = cythonize(os.path.join("myproj", "__init__.pyx")),
    packages=['myproj'],
)

