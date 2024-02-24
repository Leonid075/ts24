import pandas as pd
import numpy as np

data = pd.read_csv("students_data.csv")

maleD = data[~(data["sex"] == "M")]["Dalc"].dropna().to_numpy()
maleW = data[~(data["sex"] == "M")]["Walc"].dropna().to_numpy()

femaleD = data[~(data["sex"] == "F")]["Dalc"].dropna().to_numpy()
femaleW = data[~(data["sex"] == "F")]["Walc"].dropna().to_numpy()

print(len(maleD), len(maleW), len(femaleD), len(femaleW), len(data))

MavD_mean, MavW_mean = np.mean(maleD), np.mean(maleW)
FavD_mean, FavW_mean = np.mean(femaleD), np.mean(femaleW)

MavD_median, MavW_median = np.median(maleD), np.median(maleW)
FavD_median, FavW_median = np.median(femaleD), np.median(femaleW)

MavD_meang, MavW_meang = np.sqrt(np.square(maleD).mean()), np.sqrt(np.square(maleW).mean())
FavD_meang, FavW_meang = np.sqrt(np.square(femaleD).mean()), np.sqrt(np.square(femaleW).mean())

x = ["MaleD", "MaleW", "FemaleD", "FemaleW"]
y_mean = [MavD_mean, MavW_mean, FavD_mean, FavW_mean]
y_median = [MavD_median, MavW_median, FavD_median, FavW_median]
y_meang = [MavD_meang, MavW_meang, FavD_meang, FavW_meang]

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
sns.barplot(x=x, y=y_mean)

plt.subplot(1, 3, 2)
sns.barplot(x=x, y=y_median)

plt.subplot(1, 3, 3)
sns.barplot(x=x, y=y_meang)