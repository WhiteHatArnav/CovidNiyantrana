import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [2, 4, 6, 8, 10, 12, 14]
y = [2800000 ,3100000, 3300000, 3500000, 3650000, 3750000, 3800000]

RealModel = np.poly1d(np.polyfit(x,y, 2))
RealLine = np.linspace(1, 15, 100)
Realline2 = np.linspace(15, 30, 100)

plt.scatter(x, y,color = 'red' )

plt.plot(RealLine, RealModel(RealLine), color = 'red', label = 'Real Data Based Line') 
plt.plot(Realline2, RealModel(Realline2), color = 'red', label = 'Real Data Based Line', linestyle='dashed') 

plt.show()

