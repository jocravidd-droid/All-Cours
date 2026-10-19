"""

AUCUN RAPPORT AVEC LE COURS JUSTE POUR LE PLAISIR JE VAIS JUSTE REMETTRE UN ALGO TRES CONNU ET TRES LENT
MAIS QUI ET LE PLUS AMUSANT A FAIRE L'ALGO CE TROUVE DANS LE FICHIER "algo_champion.txt"

"""


def champion(liste):
    champion = liste[0]
    big = []
    small = []

    for l in liste:
        if l >= champion:
            big.append(l)
            champion = l
        else:
            small.append(l)

    print("GRAND CHIFFRE:", big, "PETIT CHIFFRE:", small)


champion([15, 16, 11, 13, 12])
