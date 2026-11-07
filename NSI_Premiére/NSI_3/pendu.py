from os import system
from random import choice

# ==========================================
# 1. DESSIN DU PENDU
# ==========================================


def dessinPendu(nb):  # animation de morts du pendule
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


# ==========================================
# 2. RECUPERATION DES MOTS
# ==========================================


def livre_pendu(fichier="mots.txt"):

    new_liste = []

    with open(fichier, "r", encoding="utf-8") as m:
        mots = m.read()

    liste_mots = mots.split("\n")

    for l in liste_mots:
        k = l.strip().lower()

        if k != "":
            new_liste.append(k)

    return new_liste


# ==========================================
# 3. JEU DU PENDU
# ==========================================


def game_pendu():

    system("clear")

    # Initialisation

    liste_mots = livre_pendu()

    mot_secret = choice(liste_mots)

    lettres_trouvees = []
    lettres_utilisees = []

    erreur = 0

    mot_affiche = ""

    for l in mot_secret:
        mot_affiche += "_"

    # Boucle principale

    while erreur < 6 and mot_affiche != mot_secret:
        print(dessinPendu(erreur))

        print("\nMot :", mot_affiche)
        print("Lettres utilisées :", lettres_utilisees)

        user = input("\nUne lettre : ").strip().lower()

        # Vérification de la saisie

        if len(user) != 1:
            print("Saisie invalide")

        elif user in lettres_utilisees:
            print("Lettre déjà proposée")

        else:
            lettres_utilisees.append(user)

            # Vérification de la lettre

            if user in mot_secret:
                lettres_trouvees.append(user)

                print("Bonne réponse")

            else:
                erreur += 1

                print("Mauvaise réponse")

            # Reconstruction du mot

            mot_affiche = ""

            for l in mot_secret:
                if l in lettres_trouvees:
                    mot_affiche += l

                else:
                    mot_affiche += "_"

    # ======================================
    # 4. FIN DE LA PARTIE
    # ======================================

    print(dessinPendu(erreur))
    print("\nMot :", mot_affiche)

    if mot_affiche == mot_secret:
        print("\nBravo, vous avez gagné !")

    else:
        print("\nVous avez perdu !")
        print("Le mot était :", mot_secret)


# ==========================================
# 5. LANCEMENT DU PROGRAMME
# ==========================================

if __name__ == "__main__":
    print("\n========== JEU DU PENDU ==========")

    user = input("\nPrêt ? (y or n) : ")

    if user.lower() == "y":
        game_pendu()

    elif user.lower() == "n":
        system("clear")
        print("🐇 Fin du programme. Suivez le lapin blanc...")

    else:
        print("Choix inconnu !")
