# CWiid Wiimote Interface

[![Build Status](https://travis-ci.org/azzra/python3-wiimote.svg?branch=master)](https://travis-ci.org/azzra/python3-wiimote)

## DESCRIPTION

The CWiid package contains the following parts:
1. libcwiid - wiimote API
2. cwiid module - python interface to libcwiid

## REQUIREMENTS

awk, bison, flex, bluez-libs, python 3+, python-dev for python module, kernel sources

## INSTALLATION

```sh
aclocal
autoconf
./configure
make
```

### Only Python extension

Install the library with package manager & the extension from the sources

```sh
apt-get install libcwiid1
cd python
sudo make install
```

### Library & extension

Use extension & library from sources

```sh
sudo make install
```

## Credits

Original libcwiid & Python module author: L. Donnie Smith <donnie.smith@gatech.edu>.
You can fin the original source here: https://github.com/abstrakraft/cwiid

I just made the Python extension working for Python 3.
