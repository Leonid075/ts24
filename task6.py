import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("students_data.csv")

# 6.1

maleD = data[~(data["sex"] == "M")]["Dalc"].dropna().to_numpy()
maleW = data[~(data["sex"] == "M")]["Walc"].dropna().to_numpy()

femaleD = data[~(data["sex"] == "F")]["Dalc"].dropna().to_numpy()
femaleW = data[~(data["sex"] == "F")]["Walc"].dropna().to_numpy()

print(len(maleD), len(maleW), len(femaleD), len(femaleW), len(data))

MavD_mean, MavW_mean = np.mean(maleD), np.mean(maleW)
FavD_mean, FavW_mean = np.mean(femaleD), np.mean(femaleW)

MavD_median, MavW_median = np.median(maleD), np.median(maleW)
FavD_median, FavW_median = np.median(femaleD), np.median(femaleW)

MavD_meang, MavW_meang = np.sqrt(
    np.square(maleD).mean()), np.sqrt(np.square(maleW).mean())
FavD_meang, FavW_meang = np.sqrt(
    np.square(femaleD).mean()), np.sqrt(np.square(femaleW).mean())

x = ["MaleD", "MaleW", "FemaleD", "FemaleW"]
y_mean = [MavD_mean, MavW_mean, FavD_mean, FavW_mean]
y_median = [MavD_median, MavW_median, FavD_median, FavW_median]
y_meang = [MavD_meang, MavW_meang, FavD_meang, FavW_meang]


plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
sns.barplot(x=x, y=y_mean)
plt.title("Mean")

plt.subplot(1, 3, 2)

sns.barplot(x=x, y=y_median)
plt.title("Median")

plt.subplot(1, 3, 3)
sns.barplot(x=x, y=y_meang)
plt.title("Geometric Mean")

plt.savefig("Dalc_Walc")

# 6.2
params = ["address", "Pstatus", "higher", "romantic", "freetime"]

fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(20, 3))

for ind, i in enumerate(params):
    axs[ind].set_title(i)
    sns.boxenplot(data=data, x="Dalc", y=i, ax=axs[ind])
    axs[ind].grid()

fig.tight_layout()
fig.savefig("Dalc_by")

fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(20, 3))

for ind, i in enumerate(params):
    axs[ind].set_title(i)
    sns.boxenplot(data=data, x="Walc", y=i, ax=axs[ind])
    axs[ind].grid()

fig.tight_layout()
fig.savefig("Walc_by")

# 6.3
worstG3 = data.sort_values("G3")[:50]
bestG3 = data.sort_values("G3")[::-1][:50]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(6, 3))

axs[0].set_title("Dalc")
sns.boxenplot(data=worstG3, x="G3", y="Dalc", ax=axs[0])
axs[0].grid()

axs[1].set_title("Walc")
sns.boxenplot(data=worstG3, x="G3", y="Walc", ax=axs[1])
axs[1].grid()

fig.tight_layout()
fig.savefig("walk_worst")


fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(6, 3))

axs[0].set_title("Dalc")
sns.boxenplot(data=bestG3, x="G3", y="Dalc", ax=axs[0])
axs[0].grid()

axs[1].set_title("Walc")
sns.boxenplot(data=bestG3, x="G3", y="Walc", ax=axs[1])
axs[1].grid()

fig.tight_layout()
fig.savefig("walk_best")
