// 
//  Copyright (C) 2008  Smithsonian Astrophysical Observatory
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
#include "glue.hh"
#include "beta.hh"
#include "gauss.hh"


// USER CONTENT HERE

int beta1d_proto(const double* p,
		 const double* x, const int xsize,
		 double* y, const int ysize) {
  
  beta1d<double>(x, xsize, p, y);
  
  return EXIT_SUCCESS;
  
}

int gauss1d_proto(const double* p,
		  const double* x, const int xsize,
		  double* y, const int ysize) {
  
  gauss1d<double>(x, xsize, p, y);
  
  return EXIT_SUCCESS;
  
}
int beta1d_proto_int(const double* p,
		 const double* xlo, const int xlosize,
		 const double* xhi, const int xhisize,
		 double* y, const int ysize) {
    
  return EXIT_FAILURE;
  
}

int gauss1d_proto_int(const double* p,
		  const double* xlo, const int xlosize,
		  const double* xhi, const int xhisize,
		  double* y, const int ysize) {
    
  return EXIT_FAILURE;
  
}

int beta2d_proto(const double* p,
		 const double* x0, const int x0size,
		 const double* x1, const int x1size,
		 double* y, const int ysize) {
  
  beta2d<double>(x0, x1, x0size, p, y);

  return EXIT_SUCCESS;
  
}

int gauss2d_proto(const double* p,
		  const double* x0, const int x0size,
		  const double* x1, const int x1size,
		  double* y, const int ysize) {
  
  gauss2d<double>(x0, x1, x0size, p, y);

  return EXIT_SUCCESS;
  
}

int beta2d_proto_int(const double* p,
		     const double* x0lo, const int x0losize,
		     const double* x0hi, const int x0hisize,
		     const double* x1lo, const int x1losize,
		     const double* x1hi, const int x1hisize,
		     double* y, const int ysize) {
  
  return EXIT_FAILURE;
  
}

int gauss2d_proto_int(const double* p,
		      const double* x0lo, const int x0losize,
		      const double* x0hi, const int x0hisize,
		      const double* x1lo, const int x1losize,
		      const double* x1hi, const int x1hisize,
		      double* y, const int ysize) {
  
  return EXIT_FAILURE;
  
}

// END USER CONTENT HERE

static PyMethodDef Funcs[] = {

  // Here we add function prototypes to the list of functions
  // Python will know about when this module is imported.
  //
  // Functions are added via calls to
  //
  // USERMODELFCT1D( func_proto, num_parameters ),
  //
  // where func_proto is the reference to the user-written function,
  // and num_parameters is the number of parameters of the user written
  // function.

  // USER CONTENT HERE

  USERMODELFCT1D( beta1d_proto, beta1d, 4 ),

  USERMODELFCT1D( gauss1d_proto, gauss1d, 3 ),

  USERMODELFCT2D( beta2d_proto, beta2d, 7 ),

  USERMODELFCT2D( gauss2d_proto, gauss2d, 6 ),
  
  // END USER CONTENT HERE
  
  { NULL, NULL, 0, NULL }
  
};


PyMODINIT_FUNC
init_model(void)
{ 
  import_array();
  
  Py_InitModule( (char*)"_model", Funcs );
}
