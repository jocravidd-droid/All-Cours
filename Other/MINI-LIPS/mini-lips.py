def vide():
    return []


def cons(x, L):
    L.insert(0, x)
    return L


def ajouteEnTete(L, x):
    return cons(x, L)


def supprEnTete(L):
    if estVide(L):
        return "List Empty"
    return L.pop(0), L


def estVide(L):
    return L == []


def compte(L):
    if estVide(L):
        return 0
    return len(L)


if __name__ == "__main__":
    L = vide()
    estVide(L)
    L = cons(5, cons(4, cons(3, cons(2, cons(1, cons(0, L))))))
    estVide(L)
    compte(L)
    L = ajouteEnTete(L, 6)
    compte(L)
    x, L = supprEnTete(L)
    print(x)
    compte(L)
    x, L = supprEnTete(L)
    print(x)
    compte(L)
