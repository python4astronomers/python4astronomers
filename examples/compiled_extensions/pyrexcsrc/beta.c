/* 
 *  Copyright (C) 2010  Smithsonian Astrophysical Observatory
 *
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, write to the Free Software Foundation, Inc.,
 *  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 */


#include "math.h"

/* beta1d pars = { r0, beta, pos, ampl } */

inline void beta1d(double *x, int num, double *pars, double **res) {

  double diff=0;
  int i=0;
 
  for(i = 0; i < num; i++) {

    diff = (x[i] - pars[2]) / pars[0];
    (*res)[i] = pars[3] * pow(1.0 + diff * diff, (-3.0 * pars[1]) + 0.5 );

  }
}


/* beta2d pars = { r0, xpos, ypos, ellip, theta, ampl, alpha } */

inline void beta2d(double *x0, double *x1, int num, double *pars, double **res) {

  double cosTheta=0, sinTheta=0, newX=0, newY=0, ellip2=1, radius=0,
    deltaX=0, deltaY=0, p_four=0;
  int i=0;
  
  if( 0.0 != pars[3] ) {
    
    p_four = pars[4];
    while( p_four >= 2.*M_PI )
      p_four -= 2.*M_PI;
    
    while( p_four < 0.0 )
      p_four += 2.*M_PI;
    
    cosTheta = cos(p_four);
    sinTheta = sin(p_four);
    ellip2 = (1.0 - pars[3]) * (1.0 - pars[3]);    
  }
  
  for(i = 0; i < num; i++) {
    
    radius = 0.0;
    deltaX = x0[i] - pars[1];
    deltaY = x1[i] - pars[2];
    
    if( 0.0 != pars[3] ) {
      newX = deltaX * cosTheta + deltaY * sinTheta;
      newY = deltaY * cosTheta - deltaX * sinTheta;

      if( 0.0 != ellip2 )
	radius = (newX * newX * ellip2 + newY * newY) / ellip2;
      
    } else
      radius = ( deltaX * deltaX + deltaY * deltaY );
    
    (*res)[i] = pars[5] * pow(1.0 + (radius/(pars[0]*pars[0])), -pars[6]);
    
  }
}
