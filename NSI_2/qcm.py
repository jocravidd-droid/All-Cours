import time
import json

print("""\n                  ██████╗   ██████╗ ███╗   ███╗
                 ██╔═══██╗ ██╔════╝ ████╗ ████║
                 ██║   ██║ ██║      ██╔████╔██║
                 ██║▄▄ ██║ ██║      ██║╚██╔╝██║
                 ╚██████╔╝ ╚██████╗ ██║ ╚═╝ ██║
                  ╚══▀▀═╝   ╚═════╝ ╚═╝     ╚═╝
                ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
                Q u i z  M u l t i  C h o i c e \n""")

qcm = {}
cumulateur = 0
x = []

for i in range(0, 50):
    print(f"\rChargement [{'█' * i + '░' * (50 - i)}]", end="\r", flush=True)
    time.sleep(0.1)

with open("qcm.txt", "r") as f:
    contenu = f.read()

ligne = contenu.split("\n")
for l in ligne:
    if l != "":
        a = l.strip()
        b = a.split(";;")
        x.append(b)

for y in x:
    print(y)
    qcm[y[0]] = [str(y[1])]

print(qcm)
