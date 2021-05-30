import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

TotalPop = 1360000000
HerdImmPop = 0.75  * TotalPop 

Jabs = 165000000
CovidRecovered = 300000000
TargetJabs = HerdImmPop*2 - CovidRecovered
ToBeJabbed = TargetJabs - Jabs

#Monthly Prod
CovShProd = 60000000
CovaxProd = 20000000
SputnikProd = 3000000


CovaxProdTarget = 70000000
CovShProdTarget = 65000000
OtherVaxTarget = 5000000

MonthlyVax = CovaxProd + CovShProd + SputnikProd
TargetMonthlyVax = CovaxProdTarget + CovShProdTarget + OtherVaxTarget



y = np.arange(Jabs,TargetJabs, MonthlyVax)
n = len(y)
x = range(1,n+1)




y2 = np.arange(y[3],TargetJabs, TargetMonthlyVax)
n2 = len(y2)
x2 = range(4,n2+4)


targLine = [y[n-1]] * 26

MonthRef = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']
YearRef = ['2021', '2022', '2023']

CurRateLabel = str(MonthlyVax/1000000) + ' Mil.'
TargetRateLabel = str(TargetMonthlyVax/1000000) + ' Mil.'



plt.scatter(x,y)
plt.scatter(x2, y2, color = 'green')

for i in x:
    j = y[i-1]
    if(i < 12):
        month  = MonthRef[i-1] 
    if(i >= 12): 
        month = MonthRef[(i -12-1)]

    if(i <= 7):
        xlab =  month + ' ' + YearRef[0]
    if(i > 7 and i <= 19):
        xlab = month +  ' ' + YearRef[1]
    if(i > 19):
        xlab =  month +  ' ' + YearRef[2]

    yinMil = j/1000000
    ylab =  str(yinMil) + ' Mil.'
    
    if(i == 1 or i%3 == 0 or i == n):
        if(i != n-1):
            plt.annotate( '('+ xlab + ', ' + ylab +')', (i+1,j), color = 'blue')



for i in x2:
    j = y2[i-4]
    if(i < 12):
        month  = MonthRef[i-1] 
    if(i >= 12): 
        month = MonthRef[(i -12-1)]

    if(i <= 7):
        xlab =  month + ' ' + YearRef[0]
    if(i > 7 and i <= 19):
        xlab = month +  ' ' + YearRef[1]
    if(i > 19):
        xlab =  month +  ' ' + YearRef[2]

    yinMil = j/1000000
    ylab =  str(yinMil) + ' Mil.'
    
    if(i == 2 or i%2 == 0  or i == n2+3):
        if(i != n2+2):
            plt.annotate( '('+ xlab + ', ' + ylab +')', (i-4,j), color = 'green')

plt.title('Vaccination Trend in India at Current and Government Target Rate')
plt.plot(x,y, label = 'Total Vaccine jabs at Current Rate of: ' + CurRateLabel + " Per Month")
plt.plot(x2, y2, color = 'green', label = 'Total Vaccine Jabs at Target Rate of: ' + TargetRateLabel + " Per Month")
plt.plot(targLine, color = 'red')
plt.xlabel('Number of Months from May 2020')
plt.ylabel('Total number of Covid 19 Vaccination Shots Administered in India')
plt.annotate('Target No.  of  Vaccine shots: ' + str(y[n-1]/1000000) + ' Mil.', (2, y[n-1]+10000000), color = 'red')
plt.xlim(1,25)
plt.legend()
plt.show()



