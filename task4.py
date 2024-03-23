import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("students_data.csv")

sns.catplot(data=data, x="G1", hue="Subject", kind="violin", bw_adjust=.6, cut=0, split=True,).savefig("G1.png") 
print(data[data["Subject"] == "Por"]["G1"].value_counts())
print(data[data["Subject"] == "Math"]["G1"].value_counts())
    
sns.catplot(data=data, x="G2", hue="Subject", kind="violin", bw_adjust=.6, cut=0, split=True,).savefig("G2.png") 
print(data[data["Subject"] == "Por"]["G2"].value_counts())
print(data[data["Subject"] == "Math"]["G2"].value_counts())
    
sns.catplot(data=data, x="G3", hue="Subject", kind="violin", bw_adjust=.6, cut=0, split=True,).savefig("G3.png") 
print(data[data["Subject"] == "Por"]["G3"].value_counts())
print(data[data["Subject"] == "Math"]["G3"].value_counts())