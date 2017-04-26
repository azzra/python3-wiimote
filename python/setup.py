from distutils.core import setup, Extension

setup(
    name='cwiid',
    version='3.0.0',
    description='Python3 module for libcwiid',
    author='Azzra',
    author_email='azzra@users.noreply.github.com',
    ext_modules=[Extension('cwiid', ['cwiidmodule.c', 'Wiimote.c'], libraries=['cwiid', 'bluetooth'])]
)
