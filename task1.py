import pandas as pd
import numpy as np

data = pd.read_csv("students_data.csv")
data_update = pd.read_csv("students_data(1).csv")
b = ["Subject","school","sex","address","famsize","Pstatus","Mjob","Fjob","reason","guardian","schoolsup","famsup","paid","activities","nursery","higher","internet","romantic","cheating"]
l = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]

def ren(a):
    if a == 'o':
        return "0"
    else: return a

try:
    for i in b:
        data[i] = data[i].apply(lambda x: str(x).upper())
except AttributeError:
    print(i)
    
for i in l:
    data[i] = data[i].apply(ren)
    
data.to_csv("students_data(1).csv")    