import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


CurtTotalVaxed =  514500268
DailyVaxed = 5000000
MonthlyVaxed = DailyVaxed * 30

x = range(1, 11)
y = [0] * 10
y[0] = CurtTotalVaxed

targLine = [1709000000]*16



for i in range(1,10):
    y[i] = CurtTotalVaxed + i * MonthlyVaxed


plt.title('Vaccination Trend in India at Current Rate of Increase')
plt.scatter(x,y)
plt.plot(x,y)

MonthRef = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
YearRef = ['2021', '2022', '2023']


for i in range(0, 10):
    j = y[i]
    if(i < 12):
        month  = MonthRef[i] 
    if(i >= 12): 
        month = MonthRef[(i -12)]
    if(i < 5):
        xlab =  month + ' ' + YearRef[0]
    if(i >= 5):
        xlab = month +  ' ' + YearRef[1]
    yinMil = j/1000000
    ylab =  str(yinMil) + ' Mil.'
    plt.annotate( '('+ xlab + ', ' + ylab +')', (i+1.5,j), color = 'blue')
    print(xlab)




plt.plot(targLine, color = 'red')
plt.xlim(0,15)
plt.annotate('Target No.  of  Vaccine shots: ' + str(targLine[0]/1000000) + ' Mil.', (0.25, targLine[0]+10000000), color = 'red')
plt.xlabel('Number of Months from August 2021')
plt.ylabel('Total number of Covid 19 Vaccination Shots Administered in India')
plt.show()




