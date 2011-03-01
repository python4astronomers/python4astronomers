#!/usr/bin/env python
# 
#  Copyright (C) 2011  Smithsonian Astrophysical Observatory
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


import numpy
import time
import cProfile
import pyfits

import fsrc as f
import csrc as c
import cppsrc as cc
import pysrc as py
import pyrexcsrc as pyx

def bench(func, name, *args):

    tt = time.time()
    for ii in range(1):
        result = func(*args)
    print '%s in %g secs' % (name, time.time()-tt)
    return result


def comp(func, name, tol, bench, *args):

    tt = time.time()
    for ii in range(1):
        result = func(*args)
    print '%s in %g secs' % (name, time.time()-tt)

    try:
        assert numpy.allclose(result, bench, tol, tol)
    except AssertionError:
        print '%s FAILED within tol=%g' % (name, tol)
        idx = (sao_fcmp(result,bench,tol)!=0).nonzero()[0]
        print 'max delta=%g' % (numpy.abs(result[idx]-bench[idx])).max()


def run1d():
   #1D

    x = numpy.arange(0.1,10001,0.01)
    bpars = numpy.array([ 5000., 1.2, 5120., 1020. ], dtype=float)
    gpars = numpy.array([ 10000., 5120., 1020. ], dtype=float)

    # retrieve bench mark from file
    hdu = pyfits.open('sherpa_beta1d.fits')
    sbeta = hdu[1].data.field('SHERPA_BETA1D')
    
    #_tol = float(numpy.finfo(numpy.float64).eps)
    _tol = 1.e-14

    comp(c.beta1d, 'C/C++   beta1d ', _tol, sbeta, bpars, x)
    comp(pyx.beta1d,'Pyrex C beta1d ', _tol, sbeta, bpars, x)
    comp(cc.beta1d,'C++     beta1d ', _tol, sbeta, bpars, x)
    comp(f.beta1d, 'Fortran beta1d ', _tol, sbeta, bpars, x)
    comp(py.beta1d,'Python  beta1d ', _tol, sbeta, bpars, x)
    print("")

    # retrieve bench mark from file
    hdu = pyfits.open('sherpa_gauss1d.fits')
    sgauss = hdu[1].data.field('SHERPA_GAUSS1D')

    comp(c.gauss1d, 'C/C++   gauss1d', _tol, sgauss, gpars, x)
    comp(pyx.gauss1d,'Pyrex C gauss1d', _tol, sgauss, gpars, x)
    comp(cc.gauss1d,'C++     gauss1d', _tol, sgauss, gpars, x)
    comp(f.gauss1d, 'Fortran gauss1d', _tol, sgauss, gpars, x)
    comp(py.gauss1d,'Python  gauss1d', _tol, sgauss, gpars, x)
    print("")

def run2d():

    #2D
    dim = [1280,1280]

    x = (3750, 4256)
    diff = 0.1

    x0 = numpy.arange(x[0], x[0] + (dim[0])*diff - diff/2., diff)
    x1 = numpy.arange(x[1], x[1] + (dim[1])*diff - diff/2., diff)

    pars = numpy.array([

        100.56789,
        x0[dim[0]/2-1],
        x1[dim[1]/2-1],
        0.7667777,
        numpy.pi/2.,
        7.2648566,
        1.753234

    ], dtype=float)

    X0, X1, = numpy.meshgrid(x0,x1)
    x0 = X0.ravel().copy()
    x1 = X1.ravel().copy()

    # retrieve bench mark image from file
    hdu = pyfits.open('sherpa_beta2d.fits')
    sbeta = hdu[0].data

    #_tol = float(numpy.finfo(numpy.float64).eps)
    _tol = 1.e-14

    comp(c.beta2d, 'C/C++   beta2d ', _tol, sbeta, pars, x0, x1)
    comp(pyx.beta2d,'Pyrex C beta2d ', _tol, sbeta, pars, x0, x1)
    comp(cc.beta2d,'C++     beta2d ', _tol, sbeta, pars, x0, x1)
    comp(f.beta2d, 'Fortran beta2d ', _tol, sbeta, pars, x0, x1)
    comp(py.beta2d,'Python  beta2d ', _tol, sbeta, pars, x0, x1)
    print("")

    # slice off extra beta2d pars to use for gauss2d
    pars = pars[:6]

    # retrieve bench mark image from file
    hdu = pyfits.open('sherpa_gauss2d.fits')
    sgauss = hdu[0].data 

    _tol = 1.e-12

    comp(c.gauss2d, 'C/C++   gauss2d', _tol, sgauss, pars, x0, x1)
    comp(pyx.gauss2d,'Pyrex C gauss2d', _tol, sgauss, pars, x0, x1)
    comp(cc.gauss2d,'C++     gauss2d', _tol, sgauss, pars, x0, x1)
    comp(f.gauss2d, 'Fortran gauss2d', _tol, sgauss, pars, x0, x1)
    comp(py.gauss2d,'Python  gauss2d', _tol, sgauss, pars, x0, x1)
    print("")


if __name__ == '__main__':
    run1d()
    run2d()
