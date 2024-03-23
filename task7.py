import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students_data.csv")

params1 = ["sex", "schoolsup", "famsup", "paid", "internet", ]
params2 = ["Dalc", "Walc", "traveltime", ]

fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(15, 4))

for ind, i in enumerate(params1):
    axs[ind].set_title(i)
    sns.boxenplot(data=data, x="G3", y=i, ax=axs[ind])
    axs[ind].grid()

fig.tight_layout()
fig.savefig("grade_by1")

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(18, 4))

for ind, i in enumerate(params2):
    axs[ind].set_title(i)
    sns.boxenplot(data=data, x="G3", y=i, ax=axs[ind])
    axs[ind].grid()

fig.tight_layout()
fig.savefig("grade_by2")
