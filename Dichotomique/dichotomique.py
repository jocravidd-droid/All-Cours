"""

Mini-Project : https://pixees.fr/informatiquelycee/prem/c30a.html
L'algorithme et fournis avec mon code amuser vous a le modifier ​🫡​

"""

import logging

t = [5, 7, 12, 14, 23, 27, 35, 40, 41, 45]
x = 9

# t = [5, 7, 12, 14, 23, 27, 35, 40, 41, 45]
# x = 40


def dichotomique(t, x):
    tr = False
    deb = 0
    fin = len(t)
    while tr == False and deb <= fin:
        mil = (deb + fin) // 2
        logging.debug(f"Debut : {deb} | Fin : {fin} | Milieu : {mil}")  # noqa: LOG015, PLE1205
        if t[mil] == x:
            tr = True
        else:
            if x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
    if tr:
        return "Trouver ​✅​"
    else:
        return "Introuvable ​❌​"


logging.basicConfig(level=logging.DEBUG)
x = dichotomique(t, x)
print(x)
