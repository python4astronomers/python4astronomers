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

#include <Python.h>
#include <numpy/arrayobject.h>
#include "array.hh"

#include <cmath>
#include <cfloat>

template <typename ArrayType,
	  typename DataType,
	  npy_intp NumPars,
	  int (*PtFunc)( const DataType* p, const DataType* x, 
			 const int xsize, DataType* out, 
			 const int outsize ),
	  int (*IntFunc)( const DataType* p, const DataType* xlo, 
			  const int xlosize, const DataType* xhi,
			  const int xhisize, DataType* out, 
			  const int outsize )>
PyObject* user_fct1d( PyObject* self, PyObject* args )
{
  
  ArrayType p;
  ArrayType xlo;
  ArrayType xhi;

  if( !PyArg_ParseTuple( args, (char*)"O&O&|O&",
			 CONVERTME( ArrayType ), &p,
			 CONVERTME( ArrayType ), &xlo,
			 CONVERTME( ArrayType ), &xhi ) )
    return NULL;  
    
  npy_intp npars = p.get_size();
  
  if ( NumPars != npars ) {
    PyErr_Format( PyExc_TypeError, (char*)"expected %ld parameters, got %ld",
		  long( NumPars ), long( npars ) );
    return NULL;
  }
  
  npy_intp nelem = xlo.get_size();
  
  if ( xhi && ( xhi.get_size() != nelem ) ) {
      PyErr_SetString( PyExc_TypeError,
                       (char*)"input array sizes do not match" );
      return NULL;
  }
  
  ArrayType result;
  if ( EXIT_SUCCESS != result.create( xlo.get_ndim(), xlo.get_dims() ) )
    return NULL;
  
  const DataType* pars = ( const_cast< DataType* >( &p[0] ) );
  const DataType* xlo_arr = ( const_cast< DataType* >( &xlo[0] ) );
  const DataType* xhi_arr = NULL;
  if (xhi) {
    xhi_arr = ( const_cast< DataType* >( &xhi[0] ) );
  }
  DataType* result_arr = ( const_cast< DataType* >( &result[0] ) );
  
  if ( !xhi ) {
    if (PtFunc( pars, xlo_arr, nelem, result_arr, nelem ) != EXIT_SUCCESS)
      return NULL;
  }
  else {
    if (IntFunc( pars, xlo_arr, nelem, xhi_arr, nelem, 
		 result_arr, nelem ) != EXIT_SUCCESS)
      return NULL;
  }

  return result.return_new_ref();
  
}

template <typename ArrayType,
	  typename DataType,
	  npy_intp NumPars,
          int (*PtFunc)( const DataType* p, const DataType* x0, 
			 const int x0size, const DataType* x1,
			 const int x1size, DataType* out, 
			 const int outsize ),
	  int (*IntFunc)( const DataType* p, const DataType* x0lo, 
			  const int x0losize, const DataType* x0hi, 
			  const int x0hisize, const DataType* x1lo,
			  const int x1losize, const DataType* x1hi,
			  const int x1hisize, DataType* out, 
			  const int outsize )>
PyObject* user_fct2d( PyObject* self, PyObject* args )
{
  
  ArrayType p;
  ArrayType x0lo;
  ArrayType x1lo;
  ArrayType x0hi;
  ArrayType x1hi;
  
  if ( !PyArg_ParseTuple( args, (char*)"O&O&O&|O&O&",
			  CONVERTME( ArrayType ), &p,
			  CONVERTME( ArrayType ), &x0lo,
			  CONVERTME( ArrayType ), &x1lo,
			  CONVERTME( ArrayType ), &x0hi,
			  CONVERTME( ArrayType ), &x1hi ) )
    return NULL;
  
  npy_intp npars = p.get_size();
  
  if ( NumPars != npars ) {
    PyErr_Format( PyExc_TypeError, (char*)"expected %ld parameters, got %ld",
		  long( NumPars ), long( npars ) );
    return NULL;
  }
  
  if ( x0hi && !x1hi )  {
    PyErr_SetString( PyExc_TypeError,
		     (char*)"expected 3 or 5 arguments, got 4" );
    return NULL;
  }
  
  npy_intp nelem = x0lo.get_size();
  
  if ( ( x1lo.get_size() != nelem ) ||
       ( x0hi &&
	 ( ( x0hi.get_size() != nelem ) ||
	   ( x1hi.get_size() != nelem ) ) ) ) {
    PyErr_SetString( PyExc_TypeError,
		     (char*)"input array sizes do not match" );
    return NULL;
  }
  
  ArrayType result;
  if ( EXIT_SUCCESS != result.create( x0lo.get_ndim(), x0lo.get_dims() ) )
    return NULL;
  
  const DataType* pars = ( const_cast< DataType* >( &p[0] ) );
  const DataType* x0lo_arr = ( const_cast< DataType* >( &x0lo[0] ) );
  const DataType* x1lo_arr = ( const_cast< DataType* >( &x1lo[0] ) );
  const DataType* x0hi_arr = NULL;
  const DataType* x1hi_arr = NULL;
  if (x0hi) {
    x0hi_arr = ( const_cast< DataType* >( &x0hi[0] ) );
    x1hi_arr = ( const_cast< DataType* >( &x1hi[0] ) );
  }
  DataType* result_arr = ( const_cast< DataType* >( &result[0] ) );

  if ( !x0hi ) {
    if (PtFunc( pars, x0lo_arr, nelem, x1lo_arr, nelem, 
		result_arr, nelem ) != EXIT_SUCCESS)
      return NULL;
  }
  else {
    if (IntFunc( pars, x0lo_arr, nelem, x0hi_arr, nelem,
		 x1lo_arr, nelem, x1hi_arr, nelem, 
		 result_arr, nelem ) != EXIT_SUCCESS)
      return NULL;
  }

  return result.return_new_ref();
  
}

#define FCTSPEC(name, func) \
  { (char*)#name, (PyCFunction)func, METH_VARARGS, NULL }

#define _USERMODELFCTSPEC(ptfunc, name, ftype, npars) \
  FCTSPEC(name, (ftype< DoubleArray, double, npars, ptfunc, ptfunc##_int >))

#define USERMODELFCT1D(ptfunc, name, npars) \
  _USERMODELFCTSPEC(ptfunc, name, user_fct1d, npars)
#define USERMODELFCT2D(ptfunc, name, npars) \
  _USERMODELFCTSPEC(ptfunc, name, user_fct2d, npars)
