import pandas as pd
import numpy as np

data = pd.read_csv("students_data(1).csv")
n = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]
srt = ["Mjob", "Fjob", "reason", "guardian", "romantic", "cheating", "school", "sex", "address", "famsize", "Pstatus", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "Subject"]
NMean, NGMean, NMedian, SMedian = {}, {}, {}, {}
codes = {}
    
for i in srt:
    name = i
    s = set(data[name].unique().tolist())
    codes[name] = dict(zip(s, range(len(s))))
    def code_to_num(item):
        return codes[name][item]
    data[name] = data[name].apply(code_to_num)

for i in n+srt:
    if i in n:
        NMean[i] = data[i].mean()
        NGMean[i] = np.sqrt(np.square(data[i]).mean())
        NMedian[i] = np.median(data[i])
    if i in srt:
        SMedian[i] = np.median(data[i])
    
    
print(SMedian)