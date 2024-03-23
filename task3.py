import pandas as pd
import numpy as np

dataor = pd.read_csv("students_data.csv")
data = pd.read_csv("students_data.csv")
n = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"]
srt = ["Mjob", "Fjob", "reason", "guardian", "romantic", "cheating", "school", "sex", "address", "famsize", "Pstatus", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "Subject"]
NMean, NGMean, NMedian, SMedian = {}, {}, {}, {}
codes = {}

#3.1    
for i in srt:
    # name = i
    s = set(data[i].unique().tolist())
    codes[i] = dict(zip(s, range(len(s))))
    def code_to_num(item):
        return codes[i][item]
    data[i] = data[i].apply(code_to_num)

for i in n+srt:
    if i in n:
        NMean[i] = data[i].mean()
        NGMean[i] = np.sqrt(np.square(data[i]).mean())
        NMedian[i] = np.median(data[i])
    if i in srt:
        SMedian[i] = np.median(data[i])

print(f"Среднее по числовым признакам - {NMean}\nСреднее геометрическое по числовым признакам - {NGMean}\nМедиана по числовым признакам - {NMedian}\nМедиана по категориальным признакам - {SMedian}")

#3.2
print("Сколько студентов посещают каждую из школ?")
print(f'MS - {len(dataor[dataor["school"] == "MS"])}')
print(f'GP - {len(dataor[dataor["school"] == "GP"])}')

#3.3
print("Сколько студентов посещают математику, сколько - природоведение?")
print(f'Por - {len(dataor[dataor["Subject"] == "Por"])}')
print(f'Math - {len(dataor[dataor["Subject"] == "Math"])}')

#3.4
print("Какой предмет «заваливают» чаще?")
p = sum(dataor[dataor["Subject"] == "Por"]["failures"])
m = sum(dataor[dataor["Subject"] == "Math"]["failures"])
if p > m:
    print("Por")
elif m > p: 
    print("Math")
else:
    print("Both")

#3.5
print("Сколько в среднем времени в неделю уходит на учебу по каждому предмету?")
score = "12345"
names = ["freetime", "goout", "Dalc", "Walc"]
p5, m5 = 0, 0

def rev(item):
    item = int(item)
    if int(item) >=1 and int(item) <=5:
        return int(score[-1*(score.find(str(int(item)))+1)])
    else:
        return 0
    
for i in names:
    dataor[i].fillna(0, inplace = True)
    dataor[i] = dataor[i].apply(rev)
    p5 += sum(dataor[dataor["Subject"] == "Por"][i])
    m5 += sum(dataor[dataor["Subject"] == "Math"][i])

print(p5/(4*len(dataor[dataor["Subject"] == "Por"])), m5/(4*len(dataor[dataor["Subject"] == "Math"])))

#3.6
print("На что чаще обращают внимание при выборе школы?")
print(dataor["reason"].mode().to_list()[0])