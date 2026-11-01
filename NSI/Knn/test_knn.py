from knn import f_titanic, main, median_t


def test_median_t():
    assert median_t([0, 40, 5, 7, 95, 21, 4]) == 7
    assert median_t([6, 9, 1, 8, 41, 52, 1]) == 8


def test_f_titanic():
    modele = main()
    assert (
        f_titanic(model=modele, Pclass=1, Sex=1, Age=28.0, Parch=0, Embarked=0) == 1
    ), "Regarde ce que renvoie la fonction"
    assert (
        f_titanic(model=modele, Pclass=3, Sex=0, Age=28.0, Parch=0, Embarked=0) == 0
    ), "Regarde ce que renvoie la fonction"


if __name__ == "__main___":
    test_median_t()
    test_f_titanic()
