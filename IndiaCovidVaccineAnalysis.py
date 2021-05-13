import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#Data is sourced from open source data in Google Data

ExistingInfections = 70000000
TotalPopulation = 1366400000
OverFifteenPopRatio = 0.714

TotalDosesGiven = 16800000
FullyVaccinated = 34500000


HerdImmunityThreshold = 0.8
FullVaxTarget = HerdImmunityThreshold*TotalPopulation

ImmuneAdults = 0.92*ExistingInfections + FullyVaccinated

PpltoTarget = FullVaxTarget -  ImmuneAdults
JabstoTarget = PpltoTarget*2

DurationOfEfficacy = 240

RateOfVaxing = (int)(JabstoTarget/DurationOfEfficacy)

CurrentRate = 1500000
CurrentRateReach = FullyVaccinated + CurrentRate*260

CapCurveVals = [FullyVaccinated, FullVaxTarget*2]
Indx = [0, 252]
fit = np.polyfit(Indx,CapCurveVals, 2)
CurveModel = np.poly1d(fit)
CurveLine = np.linspace(1, 240, 230)

slope = round(2*fit[0]) #second differential

SugLabelEnd = "\nRequired Ideal Constant Rate of Vaccination = " + str(RateOfVaxing) + " doses per day"
SugLabel ="\nSuggested Constant rate of increase in Daily Vaccination Rate: " + str(slope) + " doses" + SugLabelEnd 
RequiredRateData = np.arange(FullyVaccinated, FullVaxTarget*2, RateOfVaxing)

CurrentRateData = np.arange(FullyVaccinated, CurrentRateReach, CurrentRate)



plt.title("Required versus Current Number of Covid Vaccination in India\n", pad = 20) 
plt.suptitle(SugLabel, fontsize = 10, color = 'green')
plt.xlabel("Days from May 10th") 
plt.ylabel("Number of Vaccine Doses") 
plt.plot(range(0,240),RequiredRateData[0:240], label = 'Required nuumber of Vaccine Doses for herd immunity')
plt.plot(range(0,240),CurrentRateData[0:240], color = 'red', label = 'Total Vaccine Doses at Current Rate')
plt.plot(CurveLine, CurveModel(CurveLine), color = 'green', label = "Suggested Trajectory of Vaccination") 
plt.legend()
plt.show()

#print(CurrentRateData.size)









