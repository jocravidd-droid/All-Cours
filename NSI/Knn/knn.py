"""
Projet Titanic
Cours : https://pixees.fr/informatiquelycee/prem/pr5.html
Avis : Adorée
Amelioration : Le style, La fluiditer
Erreur Commis : Syntaxe, Organisation
Temps : 4h10 (en comptant les pause réflexions)
Assistance : CS50 IA (Recherche de doc)
Fonctionnement : La fonction "main()" et le cerveau deja entrainer avec les données de titanic.csv
la fonction "recherche()" utilise sont cerveau pour rechercher "x" personne en demandant au cerveau deja entrainer
graçe a la fonction "f_titanic()" qui recupere le cerveau entrainer et les info de "x" personne et effectue une predictions
Si a refaire : Je prendrais surement un peu de temps a reprendre la main mais oui c'est facile quand tu comprend exactement ce que tu dois crée
Probléme Rencontrée : Recherche de doc, Syntaxe, Reflexion, Comprehension, Erreur, Bug
Modification Possible : Cerveau, Recherche
Date : 01/11/26

"""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

pd.set_option("future.no_silent_downcasting", True)


def median_t(med):  # Trouver la moyenne
    if len(med) % 2 == 0:
        indice = len(med) // 2
        result = (med[indice] + med[indice - 1]) / 2
    else:
        indice = len(med) // 2
        result = med[indice]
    return result


def f_titanic(model, Pclass, Sex, Age, Parch, Embarked):
    x = pd.DataFrame(
        {
            "Pclass": [Pclass],
            "Sex": [Sex],
            "Age": [Age],
            "Parch": [Parch],
            "Embarked": [Embarked],
        }
    )
    prediction = model.predict(x)
    return prediction


def recherche(brain):
    try:
        name = input("\nNom : ")
        pcl = int(input("Classe Du Billet (1, 2 ou 3): "))
        if pcl != 1 and pcl != 2 and pcl != 3:
            raise ValueError("Choix Inconnu")
        s = input("Sex (male ou female): ")  # Plus à l'aise je trouve (non indicative)
        if s.lower() == "male":
            s = 0
        elif s.lower() == "female":
            s = 1
        else:
            raise ValueError("Choix Inconnu")
        ag = float(input("Age : "))
        pa = int(input("nombre de parents ou enfants à bord : "))
        embar = input("Embarquement (S, C, Q) : ")
        if embar.upper() == "S":
            embar = 0
        elif embar.upper() == "C":
            embar = 1
        elif embar.upper() == "Q":
            embar = 3
        else:
            raise ValueError("Choix Inconnu")
        if (
            isinstance(ag, float) != True
            or isinstance(pa, int) != True
            or isinstance(pcl, int) != True
        ):
            raise ValueError("Un chiffre et attendu !")
        r = f_titanic(model=brain, Pclass=pcl, Sex=s, Age=ag, Parch=pa, Embarked=embar)
        if r == 0:
            print(f"{name} : Décédé")
            return 1
        else:
            print(f"{name}: Survie")
            return 0
    except ValueError as e:
        print(f"[ERROR] : {e}")
    finally:
        print("\n🐇 Fin du programme. Suivez le lapin blanc...")


def main():
    titanic = pd.read_csv("titanic.csv")
    t = titanic.drop(
        columns=["PassengerId", "Name", "SibSp", "Ticket", "Fare", "Cabin"]
    )

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
    change_embarked = t_sans_manquants.loc[:, "Embarked"].replace(
        {"S": 0, "C": 1, "Q": 3}
    )
    t_sans_manquants["Embarked"] = change_embarked
    t_sans_manquants["Sex"] = change_sex

    x = t_sans_manquants[["Pclass", "Sex", "Age", "Parch", "Embarked"]]
    y = t_sans_manquants["Survived"]

    x_train, x_test, y_train, y_test = train_test_split(x, y)
    modele = KNeighborsClassifier()
    modele.fit(x_train, y_train)
    y_pred = modele.predict(x_test)
    pourcentage = accuracy_score(y_true=y_test, y_pred=y_pred) * 100
    if round(pourcentage, 2) > 65:
        return modele
    else:
        print(f"Pourcentage: {pourcentage:.2f}")


if __name__ == "__main__":
    modele = main()
    recherche(brain=modele)
