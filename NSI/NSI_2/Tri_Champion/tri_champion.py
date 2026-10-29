"""

AUCUN RAPPORT AVEC LE COURS JUSTE POUR LE PLAISIR JE VAIS JUSTE REMETTRE UN ALGO TRES CONNU ET TRES LENT
MAIS QUI ET LE PLUS AMUSANT A FAIRE L'ALGO CE TROUVE DANS LE FICHIER "algo_champion.txt"
AUCUN BUT RÉEL JUSTE DE LA PRATIQUE DONC NE PRENEZ PAS AU SERIEUX CE CODE IL ET TOTALEMENT DÉFECTUEUX !!

"""

def champion(liste):
    champion = liste[0]
    big = []
    small = []
    see = []

    for l in liste:
        if l in see:
            continue
        elif l >= champion:
            big.append(l)
            champion = l
            see.append(l)
        else:
            small.append(l)
            see.append(l)

    print("GRAND CHIFFRE:", big, "PETIT CHIFFRE:", small)

try:
    print("\nMETTEZ LES CHIFFRE UN PAR UN SUIVI D'UN ','")
    boxeur= input(">> ").split(',')
    k = []
    for b in boxeur:
        k.append(int(b))
    champion(k)
except ValueError:
    print("EN CHIFFRE PLS!!")
