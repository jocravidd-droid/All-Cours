#-----------------------------------------------TEST FONCTION ---------------------------------------------------------#

# convertisseur decimal en binaire
def convert_dc_bn(number, list_bin=[]):

    if number == 0:
        return number
    elif number < 0:
        return "number postivie !"

    q = number // 2

    verif = q * 2
    if verif == number: # verifie si le reste egale le chiffre de division trouver
        list_bin.append(0)
        convert_dc_bn(q) # recommence le processus de division avec le resultat de q en nombre
    else:
        list_bin.append(1) # si c'est non alors ajoute 1
        convert_dc_bn(q) # recommence le processus de division avec le resultat de q en nombre

    return list_bin[::-1]

    # convertisseur bits(binary digits) en decimal
def convert_bn_dc(number):

    digit = str(number)[::-1]
    decimal = 0

    # effectue le calcul du dernier chiffre au premier 'chiffre x 2 puissance n'
    for i, l in enumerate(digit):
        decimal += int(l) * 2**i
    return decimal
    
#-----------------------------------------------TEST FONCTION ---------------------------------------------------------#
