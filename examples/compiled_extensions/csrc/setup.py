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
from numpy.distutils.core import setup, Extension
import platform
import sys

c_libs = []
c_lib_dirs = []

if platform.system() == 'SunOS':
    c_libs.extend(['Cstd', 'sunmath'])

c_files = ['_model.cc', 'beta.c', 'gauss.c']

setup(name='model',
      ext_modules=[Extension('_model',
                             c_files,
                             library_dirs=c_lib_dirs,
                             libraries=c_libs,
                             depends=['array.hh', 'glue.hh'])]
      )
