
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import datetime
from datetime import timedelta



x = [1,2,3,4,5,6,7,8,9,10,11]
rate = [0]*11
y = [0]*11
y[0] = 330000000
rate[0] = 100000000
for i in range(1,11):
    rate[i] = rate[i-1] + 10000000

for j in range(1,11):
    y[j] = y[j-1]+rate[j-1]
targLine = [1709000000]*16
#print(y)
#print(rate)

plt.title('Vaccination Trend in India at Current Rate of Increase')
plt.scatter(x,y)
plt.plot(x,y)
plt.plot(targLine, color = 'red')
plt.xlim(0,15)
plt.annotate('Target No.  of  Vaccine shots: ' + str(targLine[0]/1000000) + ' Mil.', (4, targLine[0]+10000000), color = 'red')
plt.annotate('(April, 2022, ' + str(y[10]/1000000) + ' Mil. Shots)', (11, targLine[0]+10000000), color = 'blue')
plt.xlabel('Number of Months from June 2021')
plt.ylabel('Total number of Covid 19 Vaccination Shots Administered in India')
plt.show()