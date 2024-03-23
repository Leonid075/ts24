import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("students_data.csv")

fig = sns.violinplot(data=data, x="G1", hue="Subject", bw_adjust=.6, cut=0, split=True,)
fig = fig.get_figure()
fig.savefig("G1.png") 
print(data[data["Subject"] == "Por"]["G1"].value_counts())
print(data[data["Subject"] == "Math"]["G1"].value_counts())
fig.clear()
    
fig = sns.violinplot(data=data, x="G2", hue="Subject", bw_adjust=.6, cut=0, split=True,) 
fig = fig.get_figure()
fig.savefig("G2.png") 
print(data[data["Subject"] == "Por"]["G2"].value_counts())
print(data[data["Subject"] == "Math"]["G2"].value_counts())
fig.clear()
    
fig = sns.violinplot(data=data, x="G3", hue="Subject", bw_adjust=.6, cut=0, split=True,)
fig = fig.get_figure()
fig.savefig("G3.png") 
print(data[data["Subject"] == "Por"]["G3"].value_counts())
print(data[data["Subject"] == "Math"]["G3"].value_counts())
fig.clear()