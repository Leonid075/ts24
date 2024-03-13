import pandas as pd
import numpy as np

data = pd.read_csv("students_data.csv")

met = ["excellent", "good", "satisfactory", "unsatisfactory"]

def m(x):
    if 18 <= x <= 20:
        return met[0]
    elif 14 <= x <= 17:
        return met[1]
    elif 8 <= x <= 13:
        return met[2]
    else:
        return met[3]

G3 = data["G3"].to_numpy()
G4 = [m(i) for i in G3]

data["G4"] = G4

data.to_csv("students_data.csv")