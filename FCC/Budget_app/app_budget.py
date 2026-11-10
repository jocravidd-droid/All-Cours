# Classe représentant une catégorie de budget
class Category:
    # Initialise une catégorie avec son nom et un ledger (historique des opérations)
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Ajoute un dépôt (entrée d'argent) dans l'historique.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Effectue un retrait (sortie d'argent) si le solde est suffisant
    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        # Enregistre le retrait avec un montant négatif
        self.ledger.append({"amount": -amount, "description": description})
        return True

    # Calcule et retourne le solde en additionnant toutes les opérations
    def get_balance(self):
        return sum(t["amount"] for t in self.ledger)

    # Transfère de l'argent vers une autre catégorie
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        # Enregistre le retrait dans la catégorie actuelle
        self.withdraw(amount, f"Transfer to {category.name}")

        # Enregistre le dépôt dans la catégorie destinataire
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    # Vérifie si le solde permet d'effectuer une opération
    def check_funds(self, amount):
        return self.get_balance() >= amount

    # Définit comment afficher un objet Category sous forme de texte
    def __str__(self):

        # Centre le nom de la catégorie sur 30 caractères avec des étoiles
        header = self.name.center(30, "*")
        lines = [header]

        # Parcourt l'historique et formate chaque opération
        for t in self.ledger:
            lines.append(f"{t['description'][:23]:<23}{t['amount']:>7.2f}")

        # Ajoute le solde total à la fin de l'affichage.
        lines.append(f"Total: {self.get_balance()}")
        return "\n".join(lines)


# Génère un graphique représentant les dépenses de chaque catégorie
def create_spend_chart(categories):

    # Calcule le total des dépenses de chaque catégorie
    totals = []
    for cat in categories:
        spent = sum(-t["amount"] for t in cat.ledger if t["amount"] < 0)
        totals.append(spent)

    # Additionne les dépenses de toutes les catégories
    grand_total = sum(totals)

    # Calcule les pourcentages arrondis à la dizaine inférieure
    percentages = [int(s / grand_total * 100) // 10 * 10 for s in totals]

    # Initialise le titre du graphique
    chart = "Percentage spent by category\n"

    # Génère les barres du graphique de 100 à 0
    # Ajoute un 'o' si le pourcentage atteint le niveau actuel
    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for pct in percentages:
            line += "o  " if pct >= level else "   "
        chart += line + "\n"

    # Ajoute la ligne horizontale sous les barres
    # Sa longueur dépend du nombre de catégories
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Récupère les noms des catégories
    names = [c.name for c in categories]

    # Trouve la longueur du nom le plus long pour aligner les lettres
    max_len = max(len(name) for name in names)

    # Complète les noms avec des espaces pour avoir la même longueur
    padded = [name.ljust(max_len) for name in names]

    # Prépare les lignes qui afficheront les noms verticalement
    rows = []
    for i in range(max_len):
        row = "     "

        # Récupère la lettre à la position i de chaque nom
        # Ajoute deux espaces pour séparer les catégories
        for name in padded:
            row += name[i] + "  "

        rows.append(row)

    # Assemble toutes les lignes du graphique en une seule chaîne
    chart += "\n".join(rows)

    return chart


if __name__ == "__main__":
    # Création des catégories
    food = Category("Food")
    clothing = Category("Clothing")
    entertainment = Category("Entertainment")

    # Ajout d'argent
    food.deposit(100)
    clothing.deposit(100)
    entertainment.deposit(100)

    # Retraits (dépenses)
    food.withdraw(30, "Groceries")
    clothing.withdraw(10, "Shirt")
    entertainment.withdraw(20, "Movies")

    # Transmission de la liste des catégories en argument
    x = create_spend_chart([food, clothing, entertainment])

    print(x)
