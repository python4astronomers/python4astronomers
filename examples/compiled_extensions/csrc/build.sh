#!/bin/sh


#export CFLAGS="-mtune=core2 -finline-functions"
#export CFLAGS="-O3 -msse2 -mtune=core2 -fPIC -ffast-math -ftree-vectorize  -ftree-vectorizer-verbose=2 -funsafe-math-optimizations -fexcess-precision=fast"

#export CFLAGS="-O3 -mtune=core2 -fPIC -fopenmp"

python setup.py build_ext --inplace
