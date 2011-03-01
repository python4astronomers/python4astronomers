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

import numpy as np


# beta1d pars = { r0, beta, pos, ampl } 

def beta1d(pars, x):

    diff = (x - pars[2]) / pars[0]
    return pars[3] * np.power(1.0 + diff * diff, (-3.0 * pars[1]) + 0.5 )


# beta2d pars = { r0, xpos, ypos, ellip, theta, ampl, alpha } 

def beta2d(pars, x0, x1):

    cosTheta = 0.0; sinTheta = 0.0; ellip2 = 1.0
    if 0.0 != pars[3]:

        p_four = pars[4]

        while p_four >= 2.*np.pi:
            p_four -= 2.*np.pi

        while p_four < 0.0:
            p_four += 2.*np.pi

        cosTheta = np.cos(p_four)
        sinTheta = np.sin(p_four)
        ellip2 = (1.0 - pars[3]) * (1.0 - pars[3])


    deltaX = x0 - pars[1]
    deltaY = x1 - pars[2]

    # if 0.0 != pars[3]:
    #   newX = deltaX * cosTheta + deltaY * sinTheta
    #   newY = deltaY * cosTheta - deltaX * sinTheta

    #   if 0.0 != ellip2:
    #       radius = (newX * newX * ellip2 + newY * newY) / ellip2

    # else:
    #     radius = ( deltaX * deltaX + deltaY * deltaY )

    # return pars[5] * np.power(1.0 + (radius/(pars[0]*pars[0])), -pars[6])

    # Optimize Numpy ufuncs
    if 0.0 != pars[3]:
      newX = deltaX * cosTheta
      newX += deltaY * sinTheta
      newY = deltaY * cosTheta 
      newY -= deltaX * sinTheta

      if 0.0 != ellip2:
          radius = newX * newX
          radius *= ellip2
          radius += newY * newY
          radius /= ellip2
    else:
        radius = deltaX * deltaX
        radius += deltaY * deltaY

    result = pars[0]*pars[0]
    result = radius / result
    result += 1.0
    result = np.power(result, -pars[6])
    result *= pars[5]
    return result
