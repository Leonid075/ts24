import pandas as pd
import seaborn as sns

data = pd.read_csv("students_data.csv")
g_df = pd.DataFrame(columns=["MG1", "MG2", "MG3", "PG1", "PG2", "PG3"])

df = data.sort_values(["Subject"]).drop(["ID", "Subject", "G1", "G2", "G3", "G4",  "famrel",
                                         "freetime", "goout", "Dalc", "Walc", "absences", "cheating", "paid"], axis=1)
scores = data[["Subject", "G1", "G2", "G3"]]

duplicates = df[df.duplicated(keep=False)].sort_values(df.columns.to_list())
inds = duplicates.index.to_list()
i = iter(inds)

for _ in range(len(inds)//2):
    g_df.loc[len(g_df)] = scores.iloc[i.__next__()].tolist()[
        1:] + scores.iloc[i.__next__()].tolist()[1:]

# 8.1
print(f"Оба предмета изучали {len(g_df)} учащихся")

# 8.2
sns.displot(data=g_df, x="PG1", y="MG1", aspect=1,
            ).figure.savefig("G1_compare")
sns.displot(data=g_df, x="PG2", y="MG2", aspect=1,
            ).figure.savefig("G2_compare")
sns.displot(data=g_df, x="PG3", y="MG3", aspect=1,
            ).figure.savefig("G3_compare")
