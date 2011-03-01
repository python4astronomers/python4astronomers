# 
#  Copyright (C) 2010  Smithsonian Astrophysical Observatory
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#
#
### Python C API ###

include "Python.pxi"
include "numpy.pxi"

# Initialize numpy
import_array()

# C function prototypes
cdef extern void c_beta1d "beta1d" (double *x, int num,
                                    double *pars, double **res)

cdef extern void c_gauss1d "gauss1d" (double *x, int num,
                                      double *pars, double **res)

cdef extern void c_beta2d "beta2d" (double *x0, double *x1, int num,
                                    double *pars, double **res)

cdef extern void c_gauss2d "gauss2d" (double *x0, double *x1, int num,
                                      double *pars, double **res)

# C function signature
ctypedef void (*func_spec1d)(double *x, int num,
                           double *pars, double **res)

ctypedef void (*func_spec2d)(double *x0, double *x1, int num,
                           double *pars, double **res)

# C function wrapper
cdef object func_wrap1d(func_spec1d func, object pars, object x):

     cdef double *x_carray
     cdef double **result_carray
     cdef double *pars_carray

     cdef int xsize

     cdef ndarray pars_pyarray
     cdef ndarray x_pyarray
     cdef ndarray result_pyarray

     pars_pyarray = PyArray_ContiguousFromAny(pars, NPY_DOUBLE, 0, 0)
     x_pyarray = PyArray_ContiguousFromAny(x, NPY_DOUBLE, 0, 0)

     x_carray = <double *>x_pyarray.data
     xsize = PyArray_SIZE(x_pyarray)

     pars_carray = <double *>pars_pyarray.data

     result_pyarray = <ndarray>PyArray_SimpleNew(x_pyarray.nd,
                                                 x_pyarray.dimensions,
                                                 NPY_DOUBLE)

     result_carray = <double **>&result_pyarray.data

     func(x_carray, xsize, pars_carray, result_carray)

     return result_pyarray


cdef object func_wrap2d(func_spec2d func, object pars, object x0, object x1):

     cdef double *x0_carray
     cdef double *x1_carray
     cdef double **result_carray
     cdef double *pars_carray

     cdef int x0size
     cdef int x1size

     cdef ndarray pars_pyarray
     cdef ndarray x0_pyarray
     cdef ndarray x1_pyarray
     cdef ndarray result_pyarray

     pars_pyarray = PyArray_ContiguousFromAny(pars, NPY_DOUBLE, 0, 0)
     x0_pyarray = PyArray_ContiguousFromAny(x0, NPY_DOUBLE, 0, 0)
     x1_pyarray = PyArray_ContiguousFromAny(x1, NPY_DOUBLE, 0, 0)
          
     x0_carray = <double *>x0_pyarray.data
     x0size = PyArray_SIZE(x0_pyarray)

     x1_carray = <double *>x1_pyarray.data
     x1size = PyArray_SIZE(x1_pyarray)

     pars_carray = <double *>pars_pyarray.data

     result_pyarray = <ndarray>PyArray_SimpleNew(x0_pyarray.nd,
                                                 x0_pyarray.dimensions,
                                                 NPY_DOUBLE)

     result_carray = <double **>&result_pyarray.data

     func(x0_carray, x1_carray, x0size, pars_carray, result_carray)

     return result_pyarray


### Python ###

def beta1d(pars, x):
    return func_wrap1d(c_beta1d, pars, x)

def gauss1d(pars, x):
    return func_wrap1d(c_gauss1d, pars, x)

def beta2d(pars, x0, x1):
    return func_wrap2d(c_beta2d, pars, x0, x1)

def gauss2d(pars, x0, x1):
    return func_wrap2d(c_gauss2d, pars, x0, x1)
