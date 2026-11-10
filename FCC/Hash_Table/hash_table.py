class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        result = 0

        for i in key:
            result += ord(i)
        return result

    def add(self, key, value):
        h = self.hash(key)
        if h in self.collection:
            self.collection[h][key] = value
        else:
            self.collection[h] = {key: value}

    def remove(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            del self.collection[h][key]

    def lookup(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            return self.collection[h][key]


if __name__ == "__main__":
    # Création d'une table de hachage.
    table = HashTable()

    # Ajout de paires clé-valeur.
    table.add("name", "Mathieu")
    table.add("class", "Guerrier")
    table.add("level", "999")

    # Calcul du hash d'une clé.
    print(table.hash("name"))

    # Recherche d'une valeur à partir de sa clé.
    print(table.lookup("name"))
    print(table.lookup("level"))

    # Suppression d'une clé.
    table.remove("class")

    # Affichage de la collection.
    print(table.collection)
