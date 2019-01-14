
#To find victory of each country and finding out standard deviation mean, maximum and minimum value of each leg
import collections
from collections import defaultdict
import numpy as np
country_record=defaultdict(list)
list_of_position_avg=[[],[],[],[]]
import csv
with open('winners.csv','r') as csvfile:
	file=csv.reader(csvfile,delimiter=',')
	for row in file:
		country_record[str(row[2])].append((float(row[3])+float(row[4])+float(row[5])+float(row[6]))/60)
		for i in [0,1,2,3]:
			list_of_position_avg[i].append(float(row[i+3]))

    
country_times_won=defaultdict(int)

for key,it in country_record.items():
	country_times_won[key]=len(it)



array_one=np.array(list_of_position_avg[0])
array_two=np.array(list_of_position_avg[1])
array_three=np.array(list_of_position_avg[2])
array_four=np.array(list_of_position_avg[3])

list_of_position_record=defaultdict(list)


#print round(np.mean(array_one),2)

list_one=[np.mean(array_one),np.std(array_one),np.min(array_one),np.max(array_one)]
list_two=[np.mean(array_two),np.std(array_two),np.min(array_two),np.max(array_two)]
list_three=[np.mean(array_three),np.std(array_three),np.min(array_three),np.max(array_three)]
list_four=[np.mean(array_four),np.std(array_four),np.min(array_four),np.max(array_four)]
list_of_position_record[0].extend(list_one)
list_of_position_record[1].extend(list_two)
list_of_position_record[2].extend(list_three)
list_of_position_record[3].extend(list_four)

for val in list_of_position_record[0]:
	print val
for val in list_of_position_record[1]:
	print val
for val in list_of_position_record[2]:
	print val
for val in list_of_position_record[3]:
	print val

