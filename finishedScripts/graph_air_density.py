#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define a fit function that returns the result of a predetermined formula
def fitfunction(x,a,b,c):
    return a*np.exp(b*np.array(x)+c*np.power(np.array(x),1.5))

# Define plottable arrays
altitude = []
temp = []
gravity = []
pressure = []
density = []
viscosity = []

# Append each variable from the density.txt text file, and store each column of data in its corresponding array
with open('density.txt') as f:
    for line in f:
        data = line.split()
        altitude.append(float(data[0]))
        temp.append(float(data[1]))
        gravity.append(float(data[2]))
        pressure.append(float(data[3]))
        density.append(float(data[4]))
        viscosity.append(float(data[5]))

# Begin Plotting

# Define plot figure
fig = plt.figure()

# Add a 1x1 subplot in space 1 of the plot figure
ax1 = fig.add_subplot(1,1,1)

# Define the title, axis lables, and turn on the grid lines for subplot 1
ax1.set_title("Density")    
ax1.set_xlabel('Altitude (m)')
ax1.set_ylabel('Density (kg/m^3)')
ax1.grid(True)

# TODO not sure what this command means
ax1.set_yscale("log",nonposy='clip')

# Make the first subplot a scatter plot of Altitude vs Density
ax1.scatter(altitude,density)

# Initialize values - TODO not sure what these are, p-optimal, p-covariance?
init_vals = [10.0,-0.0001,-0.0000001]
popt, pcov = curve_fit(fitfunction, altitude, density, p0=init_vals)

# Plot the altitude array, TODO fit the altitude array with p-optimal data? With a solid red line, and Label the data with the given label
ax1.plot(altitude, fitfunction(altitude, *popt), 'r-', label = 'fit: Amplitude = %.3E, Linear = %.3E, Quadratic = %.3E' % tuple(popt))

# Include a legend for subplot 1
leg = ax1.legend()

# Display the plot
plt.show()
