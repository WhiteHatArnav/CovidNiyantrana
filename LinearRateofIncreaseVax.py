
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import datetime
from datetime import timedelta



x = [1,2,3,4,5,6,7,8,9,10,11,12]
rate = [0]*12
y = [0]*12
y[0] = 240000000
rate[0] = 90000000
for i in range(1,12):
    rate[i] = rate[i-1] + 10000000

for j in range(1,12):
    y[j] = y[j-1]+rate[j-1]

#print(y)
#print(rate)
plt.scatter(x,y)
plt.show()