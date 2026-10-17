
while True:
    menu = """
╔══════════════════════════════════════════════╗
║                  MENU PRINCIPAL              ║
╠══════════════════════════════════════════════╣
║  [0]  Décimal  →  Binaire                    ║
║  [1]  Binaire  →  Décimal                    ║
║  [2]  Quitter                                ║
╚══════════════════════════════════════════════╝
"""

    # convertisseur decimal en binaire
    def convert_dec_bin(number, list_bin=[]):

        if number == 0:
            return number
        elif number < 0:
            return "number postivie !"

        q = number // 2

        verif = q * 2
        if verif == number: # verifie si le reste egale le chiffre de division trouver
            list_bin.append(0)
            convert_dec_bin(q) # recommence le processus de division avec le resultat de q en nombre
        else:
            list_bin.append(1) # si c'est non alors ajoute 1
            convert_dec_bin(q) # recommence le processus de division avec le resultat de q en nombre

        return list_bin[::-1]

    # convertisseur bits(binary digits) en decimal
    def convert_bin_dec(number):

        digit = str(number)[::-1]
        decimal = 0

        # effectue le calcul du dernier chiffre au premier 'chiffre x 2 puissance n'
        for i, l in enumerate(digit):
            decimal += int(l) * 2**i
        return decimal

    if __name__ == "__main__":
        try:
            choice_convert = int(input(menu + "\nVotre choix : "))
            if choice_convert == 0:
                choice = int(input("\nDecimal has convert (0 for exit) : "))
                if choice == 0:
                    print("Good Bye")
                    break
                else:
                    b = convert_dec_bin(choice)
                    t = ''.join(str(number) for number in b)
                    print(f"In bits is {t}")
            elif choice_convert == 1:
                choice = int(input("\nBits has convert (0 for exit) : "))
                if choice == 0:
                    print("Good Bye")
                    break
                else:
                    b = convert_bin_dec(choice)
                    print(f"In decimal is {b}")
            elif choice_convert == 2:
                print("GOOD BYE")
                break
            else:
                print("Choice Unknow")  # type: ignore
        except ValueError:
            print("In integer pls !!")
        except (KeyboardInterrupt, EOFError):
            print("\nCLOSE PROGAMME !")
            break
