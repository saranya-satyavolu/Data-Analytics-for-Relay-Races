import sklearn
from sklearn import metrics
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import csv

with open('raceconf.csv','r') as csvfile:
	file=csv.reader(csvfile,delimiter=',')
	predicted=[]
	actual=[]
	for row in file:
		predicted.extend(row[18:21])
		actual.extend(row[21:24])


print predicted
print actual
result=confusion_matrix(actual,predicted)
print result
acc=accuracy_score(actual,predicted)
clas=classification_report(actual,predicted)

print acc
print clas
#f.write(clas)
