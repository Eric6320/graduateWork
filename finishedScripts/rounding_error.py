#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse

# This function parses and returns arguments passed in
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--choice',type=int,help='Derivative Choice',required=True)
    args = parser.parse_args()
    ichoice = args.choice
    return ichoice

# Get the choice argument from the command line
ichoice = get_args()

# Initialize variables
n = 21
xval = 1.0
dfunc, dfunch, dfunchh, xfunc, xfunchp, xfunchm, xfunchpp, xfunchmm, x, diff, difftwo = ([] for i in range(11))

# Print derivative type based on ichoice
ichoice = get_args()

n = 21
dfunc = []
dfunch = []
dfunchh = []
xfunc = []
xfunchp = []
xfunchm = []
xfunchpp = []
xfunchmm = []
x = []
diff = []
difftwo = []
xval = 1.0

if ichoice == 1:
    print "Using forward derivative ... "
elif ichoice == 2:
    print "Using centered derivative ... "
else:
    print "Using both methods ... "

# Calculate the difference between actual derivative values and approximate values given ichoice method
for i in range(0,n):

    hpower=i-n+1;
    x.append(np.power(10.0,int(hpower)));
    dfunc.append(3.0e+00*xval*xval);
    xfunc.append(xval*xval*xval);
    xfunchp.append((xval+x[i])*(xval+x[i])*(xval+x[i]));
    xfunchm.append((xval-x[i])*(xval-x[i])*(xval-x[i]));
    xfunchpp.append((xval+x[i]+x[i])*(xval+x[i]+x[i])*(xval+x[i]+x[i]));
    xfunchmm.append((xval-x[i]-x[i])*(xval-x[i]-x[i])*(xval-x[i]-x[i]));

    if ichoice == 1:
        dfunch.append((xfunchp[i]-xfunc[i])/(x[i]));
        diff.append(abs(dfunc[i]-dfunch[i]));
        print '{} {} {} {} {} {} {} {}'.format(i,x[i],xfunc[i],xfunchp[i],xfunchm[i],dfunc[i],dfunch[i],diff[i])
    elif ichoice == 2:
        dfunch.append((xfunchp[i]-xfunchm[i])/(2.0e+00*x[i]));
        diff.append(abs(dfunc[i]-dfunch[i]));
        print '{} {} {} {} {} {} {} {}'.format(i,x[i],xfunc[i],xfunchp[i],xfunchm[i],dfunc[i],dfunch[i],diff[i])
    else:
        dfunch.append((xfunchp[i]-xfunc[i])/(x[i]));
        dfunchh.append((xfunchp[i]-xfunchm[i])/(2.0e+00*x[i]));
        diff.append(abs(dfunc[i]-dfunch[i]));
        difftwo.append(abs(dfunc[i]-dfunchh[i]));
        print '{} {} {} {} {} {} {} {}'.format(i,x[i],xfunc[i],xfunchp[i],xfunchm[i],dfunc[i],dfunch[i],diff[i])


# Create the figure and add a 1x1 subplot in section 1
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("Round Error Calculation")
ax1.set_xlabel('h')
ax1.set_ylabel('Absolute Error')
ax1.set_yscale("log",nonposy='clip')
ax1.set_xscale("log",nonposy='clip')
ax1.grid(True)

# Change the plot style based on ichoice value
if ichoice == 1:
    ax1.plot(x,diff,'ro',x,diff,'r-')
elif ichoice == 2:
    ax1.plot(x,diff,'ks',x,diff,'k-')
else:
    ax1.plot(x,diff,'ro',x,diff,'r-')
    ax1.plot(x,difftwo,'ks',x,difftwo,'k-')
	
plt.show()
