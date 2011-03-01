#!/bin/bash
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


#export CC=/usr/bin/gcc
#export F77=/usr/bin/gfortran

export F77=gfortran
export F95=gfortran
export F90=gfortran

#export FFLAGS="-O3 -msse2 -ftree-vectorize -ftree-vectorizer-verbose=2 -fPIC -DF2PY_REPORT_ON_ARRAY_COPY=1 -ffast-math -funsafe-math-optimizations"
#export CFLAGS=" -DF2PY_REPORT_ON_ARRAY_COPY=1 -O3 -msse2 -ffast-math -ftree-vectorize  -ftree-vectorizer-verbose=2 -funsafe-math-optimizations"

export FFLAGS="-O3 -msse2 -fPIC -ffast-math -funroll-loops"
#export CFLAGS="-O3 -msse2 -ffast-math"

#export FFLAGS="-O0 -fPIC"


if test "x" = "x${ASCDS_INSTALL}"; then

    f2py_run="f2py"

    if test "Darwin" = `uname`; then

	#export F77=/usr/local/bin/gfortran
	f2py_run="/System/Library/Frameworks/Python.framework/Versions/Current/Extras/bin/f2py"
	#f2py_run=/data/scialg/staff/brefsdal/mac32/bin/f2py
    fi
    echo $f2py_run
    $f2py_run -m _model -c beta.f gauss.f

else
    ciaorun ${ASCDS_INSTALL}/ots/bin/f2py \
	-m _model -c beta.f gauss.f
fi
