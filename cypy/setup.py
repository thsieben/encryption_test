from distutils.core import setup
from Cython.Build import cythonize
setup(
    name= "Test Module",
    ext_modules = cythonize('program.pyx')
)
