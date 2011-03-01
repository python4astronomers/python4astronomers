This package details examples of Python code interfacing with C, CPP,
FORTRAN codes, and how each compares in execution time.  The primary focus 
is on passing NumPy arrays between C/C++/FORTRAN as function arguments.

The basic codes each implement the beta1d, beta2d, gauss1d, and gauss2d model
functions found in the Sherpa modeling and fitting package.

cppsrc:    C++ source with C++ glue

csrc:      C source with C++ glue

fsrc:      FORTRAN source with C glue (F2PY)

pyrexcsrc: C source with Cython/Pyrex generated glue

pysrc:     Python source using NumPy uFuncs


The test is run with

./build.sh
python model.py
