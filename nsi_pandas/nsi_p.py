import pandas

client = pandas.read_csv("fiches_client.csv")
commande = pandas.read_csv("fiches_com.csv")
print(client)
print("\n", commande)
cl_com = pandas.merge(client, commande)

print("\n", cl_com)
