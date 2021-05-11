import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import datetime
from datetime import timedelta

#Rounded Data from Ministry of Health And Family Welfare, Government of India and Google Data
x = [2, 4, 6, 8, 10, 12, 14]
y = [2800000 ,3100000, 3300000, 3500000, 3650000, 3750000, 3800000]

RealModel = np.poly1d(np.polyfit(x,y, 3))
RealLine = np.linspace(1, 15, 100)
RealModel2 = np.poly1d(np.polyfit(x,y, 2))
Realline2 = np.linspace(15, 35, 100)

k = RealModel.deriv().r

rofk = k[k.imag == 0].real
pt = RealModel.deriv(2)(rofk)

xmax = rofk[pt<0]
ymax = RealModel(xmax)

daystopeak = int(xmax)
strmax = "(" + str(daystopeak) + ", " + str((int)(ymax))+")"
date = datetime.datetime(2021, 4, 26) +  timedelta(days=daystopeak)

date = "\n" + date.strftime("%dth %b, %Y")

plt.scatter(x, y,color = 'red' )
plt.scatter(xmax, ymax,color = 'blue')
plt.annotate("Expected Peak\n"+ strmax+date, (xmax-3, ymax-350000), color ='blue')
plt.plot(RealLine, RealModel(RealLine), color = 'red', label = 'Real Data Based Line') 
plt.plot(Realline2, RealModel2(Realline2), color = 'red', label = 'Real Data Based Line', linestyle='dashed')
plt.xlim(1,35)
plt.title('Expected Trend of Active Covid Cases in India till End of May,', pad = 20)
plt.xlabel('Days from April 26th, 2021')
plt.ylabel('Projected Total Active Covid-19 Cases in India')
plt.show()

