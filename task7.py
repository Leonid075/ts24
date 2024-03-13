import seaborn as sns
import pandas as pd

data = pd.read_csv("students_data.csv")

sns.catplot(data=data, x="G3",  hue="sex", kind="boxen").savefig("by_sex")
sns.catplot(data=data, x="G3",  hue="traveltime", kind="boxen").savefig("by_traveltime")
sns.catplot(data=data, x="G3",  hue="schoolsup", kind="boxen").savefig("by_schoolsup")
sns.catplot(data=data, x="G3",  hue="famsup", kind="boxen").savefig("by_famsup")
sns.catplot(data=data, x="G3",  hue="paid", kind="boxen").savefig("by_paid")
sns.catplot(data=data, x="G3",  hue="internet", kind="boxen").savefig("by_internet")
sns.catplot(data=data, x="G3",  hue="Dalc", kind="boxen").savefig("by_Dalc")
sns.catplot(data=data, x="G3",  hue="Walc", kind="boxen").savefig("by_Walc")
