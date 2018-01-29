#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse

<<<<<<< HEAD
# This function parses and returns arguments passed in
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--choice',type=int,help='Derivative Choice',required=True)
=======
def get_args():
    '''This function parses and returns arguments passed in'''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c','--choice',type=int,help='Derivative Choice',required=True)
>>>>>>> f3b0a38789f328c063299a359313a26a6cc4be47
    args = parser.parse_args()
    ichoice = args.choice
    return ichoice

<<<<<<< HEAD
# Get the choice argument from the command line
ichoice = get_args()

# Initialize variables
n = 21
xval = 1.0
dfunc, dfunch, dfunchh, xfunc, xfunchp, xfunchm, xfunchpp, xfunchmm, x, diff, difftwo = ([] for i in range(11))

# Print derivative type based on ichoice
=======
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

>>>>>>> f3b0a38789f328c063299a359313a26a6cc4be47
if ichoice == 1:
    print "Using forward derivative ... "
elif ichoice == 2:
    print "Using centered derivative ... "
else:
    print "Using both methods ... "

<<<<<<< HEAD
# Calculate the difference between actual derivative values and approximate values given ichoice method
=======
>>>>>>> f3b0a38789f328c063299a359313a26a6cc4be47
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

<<<<<<< HEAD
# Create the figure and add a 1x1 subplot in section 1
fig = plt.figure()
ax1 = fig.add_subplot(111)

# Set the plot and axis titles, logarithmic scales, and turn on the plot grid
=======
fig = plt.figure()

ax1 = fig.add_subplot(111)

>>>>>>> f3b0a38789f328c063299a359313a26a6cc4be47
ax1.set_title("Round Error Calculation")
ax1.set_xlabel('h')
ax1.set_ylabel('Absolute Error')
ax1.set_yscale("log",nonposy='clip')
ax1.set_xscale("log",nonposy='clip')
ax1.grid(True)

<<<<<<< HEAD
# Change the plot style based on ichoice value
=======
>>>>>>> f3b0a38789f328c063299a359313a26a6cc4be47
if ichoice == 1:
    ax1.plot(x,diff,'ro',x,diff,'r-')
elif ichoice == 2:
    ax1.plot(x,diff,'ks',x,diff,'k-')
else:
    ax1.plot(x,diff,'ro',x,diff,'r-')
    ax1.plot(x,difftwo,'ks',x,difftwo,'k-')
	
plt.show()
