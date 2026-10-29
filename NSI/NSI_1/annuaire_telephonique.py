import time

menu = """

-----------------------------------
| 0-quitter                       |
| 1-écrire dans le répertoire     |
| 2-rechercher dans le répertoire |
-----------------------------------

"""

info = {}

print(menu)

while True:

    try:

        choix = int(input('Votre choix : '))

        # Mise a fin

        if choix == 0:
            time.sleep(0.5)
            print('\nFIN DE TACHE')
            break

        # renseignement d'informations et creation de contact

        elif choix == 1:
            while True:
                name_contact = input("Nom (0 pour terminer) : ")
                if name_contact == '0':
                    print(menu)
                    break
                else:
                    phone_number = int(input("Téléphone : "))
                    info.update({name_contact: phone_number})

        # recherche par nom en utilisant le dict 'info'

        elif choix == 2:
            search_name = input("Entrer un nom : ")
            try:
                result = info[search_name]
                print(f"Le numéro recherché est : {result}")
                time.sleep(1)
                print(menu)
            except KeyError:
                print("Le numéro recherché est Inconnu")
                time.sleep(1)
                print(menu)
    except ValueError:
        print("\nMauvaise Valeur !!\n")
    except (EOFError, KeyboardInterrupt):
        print("Interruption Forcée !")
        time.sleep(0.5)
        break

if __name__ == '__main__':

#--------------------------- zone test --------------------------------

    name_contact = "Lucas"
    phone_number = 612345678

    info.update({name_contact: phone_number})

    assert info["Lucas"] == 612345678
    assert "Lucas" in info
    assert info == {"Lucas": 612345678}

#--------------------------- zone test --------------------------------