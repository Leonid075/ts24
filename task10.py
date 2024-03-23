import pandas as pd
import numpy as np
import pickle
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def cat2num_dict(data, cat):
    cat_to_num = {}
    for i in cat:
        cat_to_num[i] = dict(
            zip(map(str, list(data[i].unique())), range(len(data[i].unique()))))
    return cat_to_num


def cat2num(data, cat, dict_):
    for i in cat:
        di = dict_[i]
        data[i] = data[i].apply(lambda x: di[str(x)])
    return data


def split(data: pd.DataFrame, seed: int = 0) -> tuple[list, list]:
    train_data, test_data = train_test_split(data.drop(
        columns=["G1", "G2", "G3"]), train_size=0.8, test_size=0.2, shuffle=True, random_state=seed)

    trainX = train_data.drop(columns=["G4"]).to_numpy()
    trainY = train_data["G4"]
    testX = test_data.drop(columns=["G4"]).to_numpy()
    testY = test_data["G4"]
    return [trainX, trainY], [testX, testY]


def train(trainX: np.ndarray, trainY: pd.Series) -> None:
    d = dict(zip(range(len(trainY.unique())), trainY.unique().tolist()))
    r = dict(zip(trainY.unique().tolist(), range(len(trainY.unique()))))

    with open("d.pkl", "wb") as file:
        pickle.dump(d, file)
    with open("r.pkl", "wb") as file:
        pickle.dump(r, file)

    def class_to_num(item):
        return r[item]

    trainY = trainY.apply(class_to_num).to_numpy()

    model = XGBClassifier(max_depth=25, n_estimators=1700,
                          enable_categorical=True)

    model.fit(trainX, trainY)

    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)


def predict(X: np.ndarray) -> list:
    with open("d.pkl", "rb") as file:
        d = pickle.load(file)

    def num_to_class(item):
        return d[item]

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    y = model.predict(X)

    return [num_to_class(i) for i in y]


def test(testX: np.ndarray, testY: pd.Series) -> float:
    predY = predict(testX)

    return accuracy_score(predY, testY)


if __name__ == "__main__":
    fit = True

    data = pd.read_csv("students_data.csv").drop(columns=["ID"])

    cat = ["Mjob", "Fjob", "reason", "guardian", "romantic", "cheating", "school", "sex", "address", "famsize",
           "Pstatus", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "Subject"]

    if fit:
        dict_ = cat2num_dict(data, cat)
        pickle.dump(dict_, open("catdict.pkl", "wb"))
    else:
        dict_ = pickle.load(open("catdict.pkl", "rb"))

    data = cat2num(data, cat, dict_)

    if fit:
        train(*split(data)[0])

    acc = test(*split(data)[1])

    print(f"Точность модели: {round(acc, ndigits=3)}")
