# CWiid Wiimote Interface

[![Build Status](https://travis-ci.org/azzra/python3-wiimote.svg?branch=master)](https://travis-ci.org/azzra/python3-wiimote)

## DESCRIPTION

The CWiid package contains the following parts:
1. libcwiid - wiimote API
2. cwiid module - python interface to libcwiid

## REQUIREMENTS

awk, bison, flex, bluez-libs, python 3.5 or greater, python dev for python module, kernel sources

## INSTALLATION

This comes with 2 parts: the libcwiid library and the Python extension.

Either you want to install just one part, you'll have to:
```sh
aclocal
autoconf
./configure
```

Then
```sh
make
sudo make install
```

> If you install only the Python extension, be sure you have the library installed (`apt-get install libcwiid1`)

## Credits

Original libcwiid & Python module author: L. Donnie Smith <donnie.smith@gatech.edu> https://github.com/abstrakraft/cwiid
I just made the Python extension working for Python3
