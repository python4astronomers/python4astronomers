c     
c     Copyright (C) 2010  Smithsonian Astrophysical Observatory
c     
c     
c     This program is free software; you can redistribute it and/or modify
c     it under the terms of the GNU General Public License as published by
c     the Free Software Foundation; either version 2 of the License, or
c     (at your option) any later version.
c     
c     This program is distributed in the hope that it will be useful,
c     but WITHOUT ANY WARRANTY; without even the implied warranty of
c     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
c     GNU General Public License for more details.
c
c     You should have received a copy of the GNU General Public License along
c     with this program; if not, write to the Free Software Foundation, Inc.,
c     51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
c
c
      
      subroutine beta1d(pars, x, num, res)
c
c     beta1d pars = { r0, beta, pos, ampl }
c
      
      integer num, i
      double precision diff, pars(4), x(num), res(num)
      
Cf2py intent(in) pars
Cf2py intent(in) x
Cf2py intent(out) res

      do i = 1, num
         diff = (x(i) - pars(3)) / pars(1)
         res(i) = pars(4) * (1.0d0 + diff * diff) 
     &        ** (-3.0d0*pars(2) + 0.5d0)
         
      enddo
      
      return
      end

      
      subroutine beta2d(pars, x0, x1, num, res)
c
c     beta2d pars = { r0, xpos, ypos, ellip, theta, ampl, alpha }
c
      
      integer num, i
      double precision pars(7), x0(num), x1(num), res(num)
      double precision cosTheta, sinTheta, newX, newY, ellip2, radius,
     &     deltaX, deltaY, p_five, pi

      parameter (pi = 3.1415926535897932d0 )

Cf2py intent(in) pars
Cf2py intent(in) x0
Cf2py intent(in) x1
Cf2py intent(out) res

      cosTheta = 0.0d0
      sinTheta = 0.0d0
      ellip2 = 1.0d0
      
      if ( 0.0d0 .ne. pars(4) ) then
         
         p_five = pars(5)
         do while ( p_five .ge. 2.d0*PI )
            p_five = p_five - 2.d0*PI
         enddo
         
         do while ( p_five .lt. 0.0d0 )
            p_five = p_five + 2.d0*PI
         enddo
         
         cosTheta = cos(p_five)
         sinTheta = sin(p_five)
         ellip2 = (1.0d0 - pars(4)) * (1.0d0 - pars(4))
         
      endif
      
      do i = 1, num
         
         radius = 0.0d0
         deltaX = x0(i) - pars(2)
         deltaY = x1(i) - pars(3)
         
         if ( 0.0d0 .ne. pars(4) ) then
            newX = deltaX * cosTheta + deltaY * sinTheta
            newY = deltaY * cosTheta - deltaX * sinTheta
            if ( 0.0d0 .ne. ellip2 ) then
               radius = (newX * newX * ellip2 + newY * newY) / ellip2
            endif
         else
            radius = ( deltaX * deltaX + deltaY * deltaY )
         endif
         
         res(i) = pars(6) * (1.0d0 + (radius/(pars(1)*pars(1))))**
     &        (-pars(7))
         
      enddo
      
      return
      end
