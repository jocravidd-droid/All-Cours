"""

ACTIVITER DE COURS DU SITE https://pixees.fr/informatiquelycee/prem/c11a.html
EN SUIVANT L'ALGORITHME DE TRI PAR INSERTION CE TROUVENT DANS LE FICHIER "algo_insert.txt"

"""

# VARIABLE
t = [15, 16, 11, 13, 12]
i = 0
j = 0
k = 0
# Debut
j = 2
while j <= len(t):
    i = j - 1
    print("1 :", i)
    k = t[j]
    if i >= 0 and t[i] > k:
        t[i + 1] = t[i]
        i = i - 1
        print("2 :", i)
    # ???

# ???
# FIN
