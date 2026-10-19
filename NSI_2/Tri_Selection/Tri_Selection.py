"""

ACTIVITER DU COURS DU SITE https://pixees.fr/informatiquelycee/prem/c11a.html
PROGRAMME FAIT EN SUIVANT L'ALGORITHME DE TRI PAR SELECTION
CE TROUVENT DANS LE FICHIER "algo_selection.txt"

"""

# VARIABLE
t = [15, 16, 11, 13, 12]
i = 0
mini = 0
j = 0
# DEBUT
i = 0
while i < len(t):
    j = i + 1
    mini = i
    while j < len(t):
        if t[j] < t[mini]:
            mini = j
        else:
            j = j + 1
    k = t[i]
    if mini != i:
        t[i] = t[mini]
        t[mini] = k
    i = i + 1

print(t)
