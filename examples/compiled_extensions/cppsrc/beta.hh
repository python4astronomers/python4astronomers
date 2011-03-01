// 
//  Copyright (C) 2010  Smithsonian Astrophysical Observatory
//
//
//  This program is free software; you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation; either version 2 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License along
//  with this program; if not, write to the Free Software Foundation, Inc.,
//  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//

#include <cmath>


// beta1d pars = { r0, beta, pos, ampl }

template <typename DataType>
static inline void beta1d(const DataType*& x, const int& num,
			  const DataType*& pars, DataType*& res) {

  DataType diff=0;
 
  for(int i = 0; i < num; i++) {

    diff = (x[i] - pars[2]) / pars[0];
    res[i] = pars[3] * std::pow(1.0 + diff * diff, (-3.0 * pars[1]) + 0.5 );

  }
}


// beta2d pars = { r0, xpos, ypos, ellip, theta, ampl, alpha }

template <typename DataType>
static inline void beta2d(const DataType*& x0, const DataType*& x1,
			  const int& num, const DataType*& pars,
			  DataType*& res) {

  DataType cosTheta=0, sinTheta=0, newX=0, newY=0, ellip2=1, radius=0,
    deltaX=0, deltaY=0, p_four=0;
  
  if( 0.0 != pars[3] ) {
    
    p_four = pars[4];
    while( p_four >= 2.*M_PI )
      p_four -= 2.*M_PI;
    
    while( p_four < 0.0 )
      p_four += 2.*M_PI;
    
    cosTheta = std::cos(p_four);
    sinTheta = std::sin(p_four);
    ellip2 = (1.0 - pars[3]) * (1.0 - pars[3]);    
  }

  for(int i = 0; i < num; i++) {
    
    radius = 0.0;
    deltaX = x0[i] - pars[1];
    deltaY = x1[i] - pars[2];

    if( 0.0 != pars[3] ) {

      newX = deltaX * cosTheta + deltaY * sinTheta;
      newY = deltaY * cosTheta - deltaX * sinTheta;

      if( 0.0 !=  ellip2 )
	radius = (newX * newX * ellip2 + newY * newY) / ellip2;
    
    } else
      radius = ( deltaX * deltaX + deltaY * deltaY );

    res[i] = pars[5] * std::pow(1.0 + (radius/(pars[0]*pars[0])), -pars[6]);
    
  }
}
