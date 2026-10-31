import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

pd.set_option("future.no_silent_downcasting", True)


def median_t(med):
    if len(med) % 2 == 0:
        indice = len(med) // 2
        result = (med[indice] + med[indice - 1]) / 2
    else:
        indice = len(med) // 2
        result = med[indice]
    return result


titanic = pd.read_csv("titanic.csv")
t = titanic.drop(columns=["PassengerId", "Name", "SibSp", "Ticket", "Fare", "Cabin"])

age = t.loc[:, "Age"]
median = []

for a in age[0:].dropna():
    median.append(a)  # noqa: PERF402
median.sort()

change_age = median_t(med=median)
embarked = t.loc[:, "Embarked"].mode()
change = {"Age": change_age, "Embarked": embarked[0]}
t_sans_manquants = t.fillna(value=change)

change_sex = t_sans_manquants.loc[:, "Sex"].replace({"male": 0, "female": 1})
change_embarked = t_sans_manquants.loc[:, "Embarked"].replace({"S": 0, "C": 1, "Q": 3})
t_sans_manquants["Embarked"] = change_embarked
t_sans_manquants["Sex"] = change_sex

x = t_sans_manquants[["Pclass", "Sex", "Age", "Parch", "Embarked"]]
y = t_sans_manquants["Survived"]

x_train, x_test, y_train, y_test = train_test_split(x, y)
modele = KNeighborsClassifier()
modele.fit(x_train, y_train)
y_pred = modele.predict(x_test)
pourcentage = accuracy_score(y_true=y_test, y_pred=y_pred) * 100
if 
