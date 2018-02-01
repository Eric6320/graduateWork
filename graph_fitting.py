#TODO include imports
import numpy as np

# A cubic function whos parameters are specified locally
generating_function(x):
	par = [1.80, -4.05, 0.40, 1.0000]
	return par[0]+par[1]*x+par[2]*x*x+par[3]*x*x*x

# Define plot figure
fig = plt.figure()
# new TCanvas("c1","Cubic Data",200,10,700,500)

# Set the order of the fitting polynomial here
m = 3

# TODO Define grid colors and set gridlines


#TODO double check this is defined correctly
n = 15 # Number of data points
x[n] = []
y[n] = []
rnd = [] # Arrays to hold xy values and fluctuations.

# TODO possibly determine a constant i, might not be necessary if its set later on
# r = math.rand #TODO figure out a random number generator

for i in range(0,n):
	# Choose an x value between -4 and 4
	x[i] = -4.0+8.0*i/n
	# Call cubic generating function
	y[i] = generating_function(x[i])
	rnd = r.Gauss(0.0, 1.5) #TODO generate a gaussian, ask what these arguments mean: rnd = r.Gaus(0.0,1.5);
	# Add random 'noise' to the data
	y[i] = y[i] + rnd

# Calculate fit parameters "by hand"
m_params = m+1
k = 0
j = 0

# TODO make sure these matrices are defined correctly
a = np.empty([m_params, m_params])
aold = np.empty([m_params, m_params])
v = np.empty([m_params, 1])

# TODO possibly determine a constant det, might not be necessary if its set later on

for k in range(0,m):
	v[k][0] = 0
	for i in range(0,n):
		v[k][0] = v[k][0] + y[i]*(x[i]**k)
	print "v[",k,"] =",v[k][0]
	for j in range(0,m):
		a[k][j] = 0
		for i in range(0,n):
			a[k][j] = a[k][j] + (x[i]**(k+j))
		print "a[",k,"][",j,"] = ",a[k][j]

aold = a

a = inv(a)
#TODO explain these operationss
#a.InvertFast(&det);
#TMatrixD U1(a,TMatrixD::kMult,aold);
#TMatrixDDiag diag1(U1); diag1=0.0;
#const Double_t U1_max_offdiag = (U1.Abs()).Max();


print " Maximum off-diagonal = ",U1_max_offdiag
print " Determinant          = ",det

# TODO explain this command as well
#TMatrixD coeff(a,TMatrixD::kMult,v);

for k in range(0,m):
	print " c[",k,"] = ",coeff[k][0]

# Fill graph object with generated data, and fit with polynomial fitting function - 3rd order polynomial

#TODO define graph object
#TODO define fit
#TODO set marker style
#TODO set title = "Cubic Fit"
#TODO setXAxisTitle "X"
#TODO setYAxisTitle "Y"

#TODO define fit line color
#TODO apply the fit to the graph
#TODO get the chi2dof value between fit and graph data
#TODO what is GetNDF
#TODO Get CHI2DOF and NDF

print "Fit 1: ",pfit1chi2," ",pfit1ndf
#TODO draw the graph

# Draw the legend
#TODO set legend size
#TODO set legend textFont
#TODO set legend textSize
#TODO set legend entry: "Fit: #chi^{2}/NDF = ",pfit1chi2ndf
#TODO draw the legend

#TODO update and actually make the graph, setting fill color and border size

#*********************************************************************************

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
