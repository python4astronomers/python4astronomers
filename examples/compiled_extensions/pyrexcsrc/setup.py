#!/usr/bin/env python
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

from numpy.distutils.core import setup
from Pyrex.Distutils.extension import Extension
from Pyrex.Distutils import build_ext

import numpy
import sys
import platform

c_libs = []
c_lib_dirs = []
c_inc_dirs = [numpy.get_include()]
c_headers = [numpy.get_include()+'/numpy/arrayobject.h']

if platform.system() == 'SunOS':
    c_libs.extend(['Cstd', 'sunmath'])

c_files = ['_model.pyx', 'beta.c', 'gauss.c']

setup(
    name='model',
    ext_modules=[ 
        Extension('_model',
                  c_files,
                  include_dirs=c_inc_dirs,
                  library_dirs=c_lib_dirs,
                  libraries=c_libs,
                  depends=c_headers),
        ],
    cmdclass = {'build_ext': build_ext}
    )
