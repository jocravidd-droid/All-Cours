from os import system
from random import choices


def dessinPendu(nb):
    tab = [
        """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
        """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """,
    ]
    return tab[nb]


def livre_pendu(fichier="mots.txt"):

    new_liste = []

    with open(fichier, "r", encoding="utf-8") as m:
        mots = m.read()
    liste_mots = mots.split("\n")
    for l in liste_mots:
        k = l.strip("\n")
        new_liste.append(k)
    return new_liste


def decoupe(secret):

    new_liste = []

    for s in secret:
        for i in s:
            new_liste.append(i)  # noqa: PERF402
    return new_liste

liste_mots = livre_pendu()
mots_secret = choices(liste_mots)
lettres_trouvees = []
letttre_utilisees = []
erreur = 0
mot_affiche = decoupe(mots_secret)

def game_pendu():
    while
    system("clear")

print("\n================ JEU DU PENDU ================")
user = input("\nPrết (y or n): ")
if user.lower() == "y":
    game_pendu()
elif user.lower() == "n":
    system("clear")
    print("🐇 Fin du programme. Suivez le lapin blanc...")
else:
    system("clear")
    raise ValueError("Choix Inconnu !")
