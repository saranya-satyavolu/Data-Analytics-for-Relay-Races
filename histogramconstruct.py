#plotting histograms with library matplotlib to visualize the statistics
import csv
import sys
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd


for i in [1,2,3,4]:
	csvfile=open('finaldata.csv','r')
	file=csv.reader(csvfile,delimiter=',')
	x=[]	
	for row in file:
		x.append(float(row[i+2]))
	print x
	arr=pd.Series(x)
	arr.hist()
	plt.show()
    

		


    
	

    




	
    
   