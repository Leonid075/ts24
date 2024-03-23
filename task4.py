import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("students_data.csv")

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20, 3))
axs[0].set_title("G1")
sns.violinplot(data=data, x="G1", hue="Subject", bw_adjust=.6, cut=0, split=True, ax=axs[0])
axs[0].grid()
print(data[data["Subject"] == "Por"]["G1"].value_counts())
print(data[data["Subject"] == "Math"]["G1"].value_counts())
    
axs[1].set_title("G2")
sns.violinplot(data=data, x="G2", hue="Subject", bw_adjust=.6, cut=0, split=True,ax=axs[1]) 
axs[1].grid()
print(data[data["Subject"] == "Por"]["G2"].value_counts())
print(data[data["Subject"] == "Math"]["G2"].value_counts())

axs[2].set_title("G3")
sns.violinplot(data=data, x="G3", hue="Subject", bw_adjust=.6, cut=0, split=True,ax=axs[2])
axs[2].grid()
print(data[data["Subject"] == "Por"]["G3"].value_counts())
print(data[data["Subject"] == "Math"]["G3"].value_counts())
fig.tight_layout()
fig.savefig("Grade")




# axs[ind].set_title(i)
# sns.boxenplot(data=data, x="G3", y="Walc", ax=axs[ind])
# axs[ind].grid()