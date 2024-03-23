import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("students_data.csv")

sns.catplot(data=data, x="G1", hue="Subject", kind="violin", bw_adjust=.6, cut=0, split=True,)
print(data[data["Subject"] == "Por"]["G1"].value_counts())
for i in range (6):
    try:
        print(data[data["Subject"] == "Por"]["G1"].value_counts()[i])
    except KeyError:
        pass
print(data[data["Subject"] == "Math"]["G1"].value_counts())
for i in range (6):
    try:
        print(data[data["Subject"] == "Math"]["G1"].value_counts()[i])
    except KeyError:
        pass
    
sns.catplot(data=data, x="G2", hue="Subject", kind="violin", bw_adjust=.6, cut=0, split=True,)
print(data[data["Subject"] == "Por"]["G2"].value_counts())
for i in range (6):
    try:
        print(data[data["Subject"] == "Por"]["G2"].value_counts()[i])
    except KeyError:
        pass
print(data[data["Subject"] == "Math"]["G2"].value_counts())
for i in range (6):
    try:
        print(data[data["Subject"] == "Math"]["G2"].value_counts()[i])
    except KeyError:
        pass
    
sns.catplot(data=data, x="G3", hue="Subject", kind="violin", bw_adjust=.6, cut=0, split=True,)
print(data[data["Subject"] == "Por"]["G3"].value_counts())
for i in range (6):
    try:
        print(data[data["Subject"] == "Por"]["G3"].value_counts()[i])
    except KeyError:
        pass
print(data[data["Subject"] == "Math"]["G3"].value_counts())
for i in range (6):
    try:
        print(data[data["Subject"] == "Math"]["G3"].value_counts()[i])
    except KeyError:
        pass