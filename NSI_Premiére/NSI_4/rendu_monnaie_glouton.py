t = [2, 1, 5, 10, 20, 50]
somme = 11


def rendu_monnaie(t, rendu, total_piece=0):
    m = sorted(t, reverse=True)

    for piece_actuelle in m:
        while rendu >= piece_actuelle:
            rendu -= piece_actuelle
            total_piece += 1
    return total_piece


x = rendu_monnaie(t, somme)
print("Total de piéce utilise : ", x)
