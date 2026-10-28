import pandas

info_villes = pandas.read_csv("villes_virgule.csv")
tri_dens = info_villes.sort_values(by=["dens"], ignore_index=True, ascending=False)

print(tri_dens)
print("La ville avec la plus grande densitée et : ", tri_dens.loc[0, "nom"])
