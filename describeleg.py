
#Basic statistical details of each leg(each runner)
import pandas as pd
import numpy as np
import csv
for i in range(1,5):
	with open('finaldata.csv','r') as csvfile:
		file=csv.reader(csvfile,delimiter=',')
		l=[]
		for row in file:
			l.append(row[i+2])
		
		arr=pd.Series(l).astype(float)
		print arr.describe()
		
	    	
		
	    
	    


