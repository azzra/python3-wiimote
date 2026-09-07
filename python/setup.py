# distutils was removed from the standard library in python 3.12: prefer
# setuptools, fall back to distutils for older pythons without setuptools.
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(
    name='cwiid',
    version='3.0.0',
    description='Python3 module for libcwiid',
    author='Azzra',
    author_email='azzra@users.noreply.github.com',
    ext_modules=[Extension('cwiid', ['cwiidmodule.c', 'Wiimote.c'], libraries=['cwiid', 'bluetooth'])]
)
