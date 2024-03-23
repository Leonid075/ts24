import pandas as pd
import seaborn as sns

data = pd.read_csv("students_data.csv")

num = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel",
       "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]
cat = ["Mjob", "Fjob", "reason", "guardian", "romantic", "cheating", "school", "sex", "address", "famsize",
       "Pstatus", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "Subject"]

sns.heatmap(data[num].corr()).figure.savefig("num_corr")
sns.heatmap(data[cat].apply(lambda x: pd.factorize(x)[0]).corr(
    method='pearson', min_periods=1)).figure.savefig("cat_corr")
