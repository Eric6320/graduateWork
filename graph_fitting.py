#TODO include imports
import numpy as np
import matplotlib.pyplot as plt

# A cubic function whos parameters are specified locally
generating_function(x):
	par = [1.80, -4.05, 0.40, 1.0000]
	return par[0]+par[1]*x+par[2]*x*x+par[3]*x*x*x

# Set the order of the fitting polynomial here
m = 3

#TODO double check this is defined correctly
n = 15 # Number of data points
x[n] = []
y[n] = []
rnd = [] # Arrays to hold xy values and fluctuations.

for i in range(0,n):
	# Choose an x value between -4 and 4
	x[i] = -4.0+8.0*i/n
	# Call cubic generating function
	y[i] = generating_function(x[i])
	#rnd = r.Gauss(0.0, 1.5) #TODO generate a gaussian, ask what these arguments mean: rnd = r.Gaus(0.0,1.5);
	rnd = np.random.normal(0.0, 1.5) # Add random 'noise' to the data
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


#******************
  
# Define some figure object with the following data:
   gStyle->SetOptFit(1);	
   TCanvas *c1 = new TCanvas("c1","Cubic Data",200,10,700,500);

# Set the fill color for the graph and turn on grid lines
   c1->SetFillColor(42);
   c1->SetGrid();

# For range 1-n, plot arrays x, and y
   TGraph *gr = new TGraph(n,x,y);
   TF1 *pfit1 = new TF1("pfit1","pol3");
# Set the market style to whatever code 21 means, possibly a shape or color combination
   gr->SetMarkerStyle(21);
# Set the plots title and axis labels
   gr->SetTitle("Cubic Fit");
   gr->GetXaxis()->SetTitle("X");
   gr->GetYaxis()->SetTitle("Y");

# Set the line colors for the fit
   pfit1->SetLineColor(2);
# Plot the fit
   gr->Fit("pfit1","q");
# Get the CHI2 value between the fit and the actual graph values
   Double_t pfit1chi2 = pfit1->GetChisquare();
# Get the number of degrees of freedom #TODO from what?
   Double_t pfit1ndf = pfit1->GetNDF();
# Print the above information to the screen
   Double_t pfit1chi2ndf = pfit1chi2/pfit1ndf;
   printf("Fit 1: %f %f \n",pfit1chi2,pfit1ndf);
   gr->Draw("AP");

# Add the legend #TODO what do the arguments represent?
   Char_t message[80];
   TLegend *legend=new TLegend(0.4,0.15,0.88,0.35);
# Set the text font for the legend
   legend->SetTextFont(72);
# Set the text size for the legend
   legend->SetTextSize(0.04);
# Add the data and fit entries to the legend
   legend->AddEntry(gr,"Data","lpe");
   sprintf(message,"Fit: #chi^{2}/NDF = %.5f",pfit1chi2ndf);
   legend->AddEntry(pfit1,message);
//   legend->Draw();

# TCanvas::Update() draws the frame, after which one can change it
   c1->Update();
   c1->GetFrame()->SetFillColor(21);
   c1->GetFrame()->SetBorderSize(12);
   c1->Modified();
