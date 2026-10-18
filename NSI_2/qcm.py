import time
import os
import random

rouge = "\033[31m"
vert = "\033[32m"
bleu = "\033[34m"
reset = "\033[0m"


def afficher_banniere():
    print(f"""\n{vert}                  ██████╗   ██████╗ ███╗   ███╗
                 ██╔═══██╗ ██╔════╝ ████╗ ████║
                 ██║   ██║ ██║      ██╔████╔██║
                 ██║▄▄ ██║ ██║      ██║╚██╔╝██║
                 ╚██████╔╝ ╚██████╗ ██║ ╚═╝ ██║
                  ╚══▀▀═╝   ╚═════╝ ╚═╝     ╚═╝
                ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
                Q u i z  C h o i c e  M u l t i{reset}\n""")


afficher_banniere()
print("\033[s", end="")
qcm = {}
cumulateur = 0
x = []

for i in range(51):
    print(
        f"\r{vert}Chargement [{'█' * i + '░' * (50 - i)}]{reset}",
        end="",
        flush=True,
    )
    time.sleep(0.1)

print()


def charger_qcm():
    with open("qcm.txt", "r", encoding="utf-8") as f:
        contenu = f.read()

    ligne = contenu.split("\n")
    for l in ligne:
        a = l.strip()
        b = a.split(";;")
        if b[0] != "" and b[1] != "":
            if len(b[0]) != 0 and len(b[1]) != 0:
                x.append(b)

    for y in x:
        if y[0] in qcm:
            print(f"{rouge}[ERROR] Double Question{reset}")
        else:
            qcm[y[0]] = y[1]


charger_qcm()
print("\033[u", end="", flush=True)

time.sleep(1)
os.system("clear")


def extraire_choix(c):
    majuscule = ["A", "B", "C", "D", "E"]
    choix = []

    for m in majuscule:
        ch = f"{m}-" in c
        if ch == True:
            choix.append(m)

    return choix


if __name__ == "__main__":
    afficher_banniere()
    q = list(qcm.keys())

    if len(q) >= 10:
        while True:
            score = 0
            carte = random.sample(q, k=10)
            qcm_choice = {}

            for c in carte:
                r = extraire_choix(c)
                qcm_choice[c] = r

            for question in qcm_choice.keys():
                print("\n", question)
                joueur = input("\n>> ").strip()
                if joueur.upper() not in qcm_choice[question]:
                    print("Hmm, je connais pas cette réponse !!")
                elif joueur.upper() == qcm[question]:
                    print("Bien joué !")
                    score += 1
                    cumulateur += 1
                else:
                    print(f"Bien essayé, mais c'était '{qcm[question]}'")

            print(f"\nScore {score} sur 10")
            demande = input(f"[{cumulateur}] | C (CONTINUE), E (EXIT) : ")
            if demande.upper() == "E":
                break
            elif demande.upper() == "C":
                os.system("clear")
                continue
            else:
                print(f"{rouge}[ERROR] CHOIX INCONNU{reset}")
                time.sleep(0.9)
                os.system("clear")
                continue
    else:
        print(f"{rouge}Minimum de 10 questions{reset}")
        os.system("open https://pixees.fr/informatiquelycee/prem/pr2.html")

print("GOOD BYE CHAMPION")
time.sleep(1)
