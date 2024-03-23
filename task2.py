import pandas as pd

df = pd.read_csv("students_data.csv")

print("Пропущенные значения:")
print(df.isnull().sum())

dfc = df.drop("cheating", axis=1).dropna()

dfc.to_csv("students_data1.csv", index=False)
