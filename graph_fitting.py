#TODO include imports

#include <ostream>
#include "TMatrixD.h"
#include "TRandom.h"

# A cubic function whos parameters are specified locally TODO figure out how to feed in arguments
generating_function(x):
	par = [1.80, -4.05, 0.40, 1.0000]
	return par[0]+par[1]*x+par[2]*x*x+par[3]*x*x*x

# TODO define a plot here
# new TCanvas("c1","Cubic Data",200,10,700,500)

# Set the order of the fitting polynomial here #TODO possibly make this a command line choice
m = 3

# TODO Define grid colors and set gridlines

n = 15 # Number of data points
x[n], y[n], rnd, = [] # Arrays to hold xy values and fluctuations. #TODO double check this is defined correctly

# TODO possibly determine a constant i, might not be necessary if its set later on
# r = math.rand #TODO figure out a random number generator
#**********************************************
void graph_fitting() {
  
   for (i=0;i<n;i++){
	   x[i]=-4.0+8.0*i/n;  // choose x betwen -4 and 4
	   y[i]=generating_function(x[i]); // call generating function
	   rnd = r.Gaus(0.0,1.5); 
	   y[i]=y[i]+rnd; // add some random "noise" to data
   }

//
// Use ROOT's linear algebra package to calculate fix parameters "by hand"
//

   const Int_t m_params = m+1;
   Int_t k = 0;
   Int_t j =0;

   TMatrixD a(m_params,m_params);
   TMatrixD aold(m_params,m_params);
   TMatrixD v(m_params,1);
   Double_t det;

   for (k=0;k<=m;k++){
	   v[k][0]=0;
	   for (i=0; i<n; i++){
			   v[k][0]=v[k][0]+y[i]*pow(x[i],k);
	   }
	   cout << "v[" << k << "] =" << v[k][0] << endl;
	   for (j=0; j<=m; j++){
		   a[k][j]=0;
	   	   for (i=0; i<n; i++){
			   a[k][j]=a[k][j]+pow(x[i],k+j);
	   	   }		
		   cout << "a[" << k << "][" << j << "] = " << a[k][j] << endl;
	   }
   }

   aold = a;

   a.InvertFast(&det);
   TMatrixD U1(a,TMatrixD::kMult,aold);
   TMatrixDDiag diag1(U1); diag1=0.0;
   const Double_t U1_max_offdiag = (U1.Abs()).Max();
   cout << " Maximum off-diagonal = " << U1_max_offdiag << endl;
   cout << " Determinant          = " << det << endl;

   TMatrixD coeff(a,TMatrixD::kMult,v);
   for (k=0;k<=m;k++){
   	cout << " c[" << k << "] = " << coeff[k][0] << endl;
   }	

//
// Fill TGraph object with generated data, and fit with ROOT's 
// built-in polynomial fitting function - p3 = 3rd order polynomial
//

   TGraph *gr = new TGraph(n,x,y);
   TF1 *pfit1 = new TF1("pfit1","pol3");
   gr->SetMarkerStyle(21);
   gr->SetTitle("Cubic Fit");
   gr->GetXaxis()->SetTitle("X");
   gr->GetYaxis()->SetTitle("Y");

   pfit1->SetLineColor(2);
   gr->Fit("pfit1","q");
   Double_t pfit1chi2 = pfit1->GetChisquare();
   Double_t pfit1ndf = pfit1->GetNDF();
   Double_t pfit1chi2ndf = pfit1chi2/pfit1ndf;
   printf("Fit 1: %f %f \n",pfit1chi2,pfit1ndf);
   gr->Draw("AP");

   // draw the legend
   Char_t message[80];
   TLegend *legend=new TLegend(0.4,0.15,0.88,0.35);
   legend->SetTextFont(72);
   legend->SetTextSize(0.04);
   legend->AddEntry(gr,"Data","lpe");
   sprintf(message,"Fit: #chi^{2}/NDF = %.5f",pfit1chi2ndf);
   legend->AddEntry(pfit1,message);
//   legend->Draw();

   // TCanvas::Update() draws the frame, after which one can change it
   c1->Update();
   c1->GetFrame()->SetFillColor(21);
   c1->GetFrame()->SetBorderSize(12);
   c1->Modified();
}
