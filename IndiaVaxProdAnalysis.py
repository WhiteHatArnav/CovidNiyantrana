import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

TotalPop = 1360000000
HerdImmPop = 0.75  * TotalPop 

Jabs = 215000000
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
TargetMonthlyVax = 300000000

TargetJabs2 = 2000000000

y = np.arange(Jabs,TargetJabs, MonthlyVax)
n = len(y)
x = range(1,n+1)



y2 = np.arange(y[2],TargetJabs2, TargetMonthlyVax)
n2 = len(y2)
x2 = range(3,n2+3)

y3 = np.arange(y[3],TargetJabs, TargetMonthlyVax)
n3 = len(y2)
x3 = range(4,n2+4)



targLine = [y[n-1]] * 26

MonthRef = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']
YearRef = ['2021', '2022', '2023']

CurRateLabel = str(MonthlyVax/1000000) + ' Mil.'
TargetRateLabel = str(TargetMonthlyVax/1000000) + ' Mil.'



plt.scatter(x,y)
plt.scatter(x2, y2, color = 'green')

for i in range(0, n):
    j = y[i]
    
    if(i < 12):
        month  = MonthRef[i] 
    if(i >= 12): 
        month = MonthRef[(i -12)]

    if(i <= 7):
        xlab =  month + ' ' + YearRef[0]
    if(i > 7 and i <= 19):
        xlab = month +  ' ' + YearRef[1]
    if(i > 19):
        xlab =  month +  ' ' + YearRef[2]

    yinMil = j/1000000
    ylab =  str(yinMil) + ' Mil.'
    
    if(i == 0 or i%3 == 0 or i == n-1):
        plt.annotate( '('+ xlab + ', ' + ylab +')', (i+1.5,j-25000000), color = 'blue')


for i in range(0,n2):
    j = y2[i]
    if(i < 12):
        month  = MonthRef[i+2] 
    if(i >= 12): 
        month = MonthRef[(i -12+2)]

    if(i <= 7):
        xlab =  month + ' ' + YearRef[0]
    if(i > 7 and i <= 19):
        xlab = month +  ' ' + YearRef[1]
    if(i > 19):
        xlab =  month +  ' ' + YearRef[2]

    yinMil = j/1000000
    ylab =  str(yinMil) + ' Mil.'
    print(j)
    plt.annotate( '('+ xlab + ', ' + ylab +')', (i-1.25,j-25000000), color = 'green')

plt.title('Vaccination Trend in India at Current and Government Target Rate')
plt.plot(x,y, label = 'Total Vaccine jabs at Current Rate of: ' + CurRateLabel + " Per Month")
plt.plot(x2, y2, color = 'green', label = 'Total Vaccine Jabs at Target Rate of: ' + TargetRateLabel + " Per Month")
plt.plot(targLine, color = 'red')
plt.xlabel('Number of Months from May 2021')
plt.ylabel('Total number of Covid 19 Vaccination Shots Administered in India')
plt.annotate('Target No.  of  Vaccine shots: ' + str(y[n-1]/1000000) + ' Mil.', (8, y[n-1]+10000000), color = 'red')
plt.xlim(0,25)
plt.ylim(125000000,1900000000)
plt.legend()
plt.show()



