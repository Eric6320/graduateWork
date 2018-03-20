# root_find - Program to find the roots of a polynomial of degree
# three using Bisection Method.
#
# Author:  Edward J. Brash
#

#include <iostream>
#include <math.h>

using namespace std



  # Initialize the polynomial
  a0 = 1.80
  a1 = -4.05
  a2 = 0.40
  a3 = 1.00

  # initialize variables
  f, xmid, fa, fb, fc

  xlow = -4.0
  xhigh = 4.0
  npoints = 10000
  xval[npoints]
  yval[npoints]
  dx = (xhigh-xlow)/npoints

  for (i = 0 i<npointsi++):
	xval[i]=xlow+i*dx
	yval[i]=a0+a1*xval[i]+a2*xval[i]*xval[i]+a3*xval[i]*xval[i]*xval[i]
	# cout << "x: " << xval[i] << "  y: " << yval[i] << endl
  	

  # Search the arrays for sign changes
  
  nsearch
  cout << "Enter the division size: "
  cin >> nsearch
  cout << endl

  niter = npoints/nsearch
  ycomp=yval[0]
  nsteps=0

  for (i=1 i<niter i++):
	y=yval[nsearch*i]
	cout << " y = " << y << endl
	nsteps++
	if (y*ycomp < 0.0):
		# Found a root in this interval
		xlow = xval[nsearch*(i-1)]
		xhigh = xval[nsearch*i]
		nsteps=nsteps+2
  		epsilon = 1.0E-10
  		diff = 1.0E12
		while (diff > epsilon):
			fa = a0 + a1*xlow + a2*xlow*xlow + a3*xlow*xlow*xlow
			fb = a0 + a1*xhigh + a2*xhigh*xhigh + a3*xhigh*xhigh*xhigh
			xmid = (xhigh + xlow)/2.0
			fc = a0 + a1*xmid + a2*xmid*xmid + a3*xmid*xmid*xmid
			product = fa*fc
			if (product < 0):
				xhigh = xmid
				fb = fc
			 else:
				xlow = xmid
				fa = fc
			

			diff = abs(fc)
			nsteps=nsteps+8
		 
		cout << "Found root at x = " << xmid << endl
		ycomp=y
		nsteps++
	
	else:
		ycomp=y
		nsteps++
	
  

  cout << "Total number of steps = " << nsteps << endl

 return 0


