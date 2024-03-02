import pandas as pd
import numpy as np

data = pd.read_csv("students_data(1).csv")
l = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]
lMean, lGMean, lMedian = dict(), dict(), dict()

for i in l:
    lMean[i] = data[i].mean()
    lGMean[i] = np.sqrt(np.square(data[i]).mean())
    lMedian[i] = np.median(data[i])
    
print(lGMean)
print(lMedian)