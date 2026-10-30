import pandas as pd

titanic = pd.read_csv("titanic.csv")
t = titanic.drop(columns=["PassengerId", "Name", "SibSp", "Ticket", "Fare", "Cabin"])
age = t.loc[:, "Age"]
median = []
for a in age[0:].dropna():
    median.append(a)  # noqa: PERF402
median.sort()
if len(median) % 2 == 0:
    indice = len(median) // 2
    result = (median[indice] + median[indice - 1]) / 2
else:
    indice = len(median) // 2
    result = median[indice]
embarked = t.loc[:, "Embarked"].mode()
change_age = {"Age": result, "Embarked": embarked[0]}
t_sans_manquants = t.fillna(value=change_age)
# Reprise Demain 31 Octobre
