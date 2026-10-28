import pandas

iden = pandas.read_csv("ident_virgule.csv")
info = iden.loc[[0, 1], ["nom", "date_naissance"]]
print(info)
