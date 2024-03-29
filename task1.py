import pandas as pd
import numpy as np

data = pd.read_csv("students_data.csv")
a = ["school", "sex", "address", "famsize", "Pstatus"]
b = ["Mjob", "Fjob", "reason", "guardian", "schoolsup", "famsup", "paid",
     "activities", "nursery", "higher", "internet", "romantic", "cheating"]
l = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel",
     "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]


def chNumb(a):
    if a == 'o':
        return "0"
    else:
        return a


def run():
    for i in a:
        data[i].fillna('', inplace=True)
        data[i] = data[i].apply(lambda x: str(x).upper())

    for i in b:
        data[i].fillna('', inplace=True)
        data[i] = data[i].apply(lambda x: str(x).lower())

    for i in l:
        data[i] = data[i].apply(chNumb)

    data.to_csv("students_data.csv", index=False)


if __name__ == '__main__':
    run()
