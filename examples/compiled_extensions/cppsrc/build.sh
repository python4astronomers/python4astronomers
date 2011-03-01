#!/bin/sh

#export CFLAGS="-mtune=core2"

# -funroll-loops  -fprofile-use

python setup.py build_ext --inplace
