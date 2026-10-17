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
    print(f"\rChargement [{'█' * i + '░' * (50 - i)}]", end="", flush=True)
    time.sleep(0)

with open("qcm.txt", "r") as f:
    contenu = f.read()

str(contenu)
print(contenu.split(";;"))
