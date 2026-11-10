import sqlite3


def main(t, search=False):
    conn = sqlite3.connect("contact.db")
    cur = conn.cursor()

    if search == False:
        datas = [t]

        cur.execute(
            "CREATE TABLE IF NOT EXISTS REPERTOIRE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, auteur TEXT, nom TXT, numero INT)"
        )
        cur.executemany(
            "INSERT INTO REPERTOIRE(auteur, nom, numero) VALUES(?, ?, ?)", datas
        )
        conn.commit()

        cur.close()
        conn.close()
    else:
        check = cur.execute(f"SELECT nom, numero FROM REPERTOIRE WHERE nom='{t}'")
        c = check.fetchall()

        cur.close()
        conn.close()

        return c[0][1]


def add_contact():
    try:
        test = False
        auteur = str(input("\nTon nom: "))
        name = str(input("Nom du contact: "))
        number = str(input("Numero a ajouter: ")).strip(" ").split(" ")
        collage = ""
        for n in number:
            collage += n
        if test == False:
            main((auteur, name, collage))
        return 0
    except ValueError as e:
        print(f"[ERROR]: {e}")


def search_contact():
    try:
        nom = str(input("\nNom Rechercher: "))
        result = main(nom, search=True)
        return result
    except ValueError as e:
        print(f"[ERROR]: {e}")


if __name__ == "__main__":
    while True:
        try:
            print("\nRépertoire Téléphonique ☎️".center(60))
            print("\nMenu")
            print("Ajouter un numero (a)")
            print("Rechercher un numero (r)")
            response = str(input("\nChoix : "))
            if response.lower() == "a":
                add_contact()
            elif response.lower() == "r":
                print("Numero: ", search_contact())
            else:
                print("Choix Inconnu")
        except ValueError as e:
            print(f"[ERROR]: {e}")
