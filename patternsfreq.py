#Finding the frequencies of different patterns

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import csv
with open('patternsdata.csv','r') as csvfile:
	file=csv.reader(csvfile,delimiter=',')

	x=['---','-+-','--+','-++','+-+','+--']
	y=[32,96,32,29,2,9]
	plt.xlabel('Pattern')
	plt.ylabel('Frequency')
	plt.plot(x,y)
	plt.show()

