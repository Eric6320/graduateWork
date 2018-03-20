import numpy as np

# root_find - Program to find the roots of a polynomial of degree three using Bisection Method.
# Author:  Edward J. Brash

# Initialize the polynomial

a0 = 1.80
a1 = -4.05
a2 = 0.40
a3 = 1.00

xlow = -4.0
xhigh = 4.0
npoints = 10000

xval = np.empty(npoints, dtype=object)
yval = np.empty(npoints, dtype=object)
dx = (xhigh-xlow)/npoints

for i in range(npoints):
	xval[i] = xlow + i*dx
	yval[i] = a0 + a1*xval[i] + a2*xval[i]*xval[i] + a3*xval[i]*xval[i]*xval[i]
	print "x: ", xval[i], "  y: ", yval[i]

#Search the arrays for sign changes

nsearch = int(raw_input("Enter the division size: "))
niter = npoints/nsearch
ycomp = yval[0]
nsteps = 0
  
for i in range(1,niter):
	y = yval[nsearch*i]
	if (y == 0.0):
		print "Found root at x = ", xval[nsearch*i]
		nsteps += 1

	nsteps += 1
	if (y*ycomp < 0.0):
		# Found a root in this interval
		xlow = xval[nsearch*(i-1)]
		xhigh = xval[nsearch*i]
		nsteps += 2
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
			nsteps += 8

		print "Found root at x = ", xmid
		ycomp = y
		nsteps += 1
	else:
		ycomp = y
		nsteps += 1

print "Total number of steps = ", nsteps
