# config reçoit le dictionnaire transmis lors de l'appel
# setting_pair reçoit un tuple (clé, valeur)
def add_setting(config, setting_pair):

    # Récupère la clé et la valeur, les transforme en string, puis les convertit en minuscules
    key = str(setting_pair[0]).lower()
    value = str(setting_pair[1]).lower()

    # Vérifie si la clé existe déjà dans le dictionnaire
    if key in config:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    else:
        # Ajoute une nouvelle paire clé-valeur au dictionnaire
        config[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


# Modifie la valeur d'une clé déjà existante
def update_setting(config, setting_pair):

    # Récupère la clé et la valeur, les transforme en string, puis les convertit en minuscules
    key = str(setting_pair[0]).lower()
    value = str(setting_pair[1]).lower()

    # Vérifie si la clé existe avant de modifier sa valeur
    if key in config:
        # Remplace l'ancienne valeur par la nouvelle
        config[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# Supprime un paramètre du dictionnaire
def delete_setting(config, chavo):

    # Convertit le nom de la clé en minuscules, puis la transforme en string, puis les convertit en minuscules
    clée = str(chavo).lower()

    # Vérifie si la clé existe
    if clée in config:
        # pop() supprime la clé et sa valeur
        config.pop(clée)
        return f"Setting '{clée}' deleted successfully!"
    else:
        return "Setting not found!"


# Affiche les paramètres contenus dans le dictionnaire
def view_settings(config):

    # Vérifie si le dictionnaire est vide
    if config == {}:
        return "No settings available."
    else:
        setting = "Current User Settings:\n"
        # items() permet de parcourir les clés et les valeurs
        for clé, valeur in config.items():
            # capitalize() met la première lettre en majuscule
            setting += f"{clé.capitalize()}: {valeur}\n"
        return setting


if __name__ == "__main__":
    # Création d'un dictionnaire contenant des paramètres
    test_settings = {"théme": "sombre", "températur": 36, "Mode Game": True}

    add_setting(test_settings, ("volume", "high"))
    update_setting(test_settings, ("températur", "38"))
    delete_setting(test_settings, ("théme"))

    # Le résultat de la fonction est stocké dans x
    x = view_settings(test_settings)
    print(x)
