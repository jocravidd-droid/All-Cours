from config_manager import add_setting, delete_setting, update_setting, view_settings

config = {
    "name": "mathieu",
    "class": "guerrier",
    "level": 999,
    "cheat": "y",
    "xp": "x2",
    "password": 846842,
}


def test_add_setting():
    temporaire = ("System", "Linux", "Parrain", "4F58A4", "level", 0)
    test_config = config.copy()

    # Vérifie qu'on ne peut pas ajouter une clé déjà existante.
    assert (
        add_setting(test_config, (temporaire[-2], str(temporaire[-1])))
        == f"Setting '{temporaire[-2]}' already exists! Cannot add a new setting with this name."
    ), "La fonction ne détecte pas une clé déjà existante !"

    # Vérifie qu'on peut ajouter une nouvelle clé.
    assert (
        add_setting(test_config, (temporaire[0], temporaire[1]))
        == f"Setting '{temporaire[0].lower()}' added with value '{temporaire[1].lower()}' successfully!"
    ), "La fonction ne fait aucun ajout !"

    # Vérifie que la nouvelle paire existe dans le dictionnaire.
    assert test_config["system"] == "linux", "La paire n'a pas été ajoutée !"


def test_update_setting():
    test_config = config.copy()

    # Vérifie la modification d'une clé existante.
    assert (
        update_setting(test_config, ("level", "1000"))
        == "Setting 'level' updated to '1000' successfully!"
    ), "La fonction ne modifie pas la valeur !"

    # Vérifie que la valeur a réellement été modifiée.
    assert test_config["level"] == "1000", "La valeur n'a pas été modifiée !"

    # Vérifie qu'on ne peut pas modifier une clé inexistante.
    assert (
        update_setting(test_config, ("mana", "50"))
        == "Setting 'mana' does not exist! Cannot update a non-existing setting."
    ), "La fonction accepte une clé inexistante !"


def test_delete_setting():
    test_config = config.copy()

    # Vérifie la suppression d'une clé existante.
    assert (
        delete_setting(test_config, "cheat") == "Setting 'cheat' deleted successfully!"
    ), "La fonction ne supprime pas la clé !"

    # Vérifie que la clé a réellement disparu.
    assert "cheat" not in test_config, "La clé existe toujours !"

    # Vérifie le comportement avec une clé inexistante.
    assert delete_setting(test_config, "mana") == "Setting not found!", (
        "La fonction ne détecte pas une clé inexistante !"
    )


def test_view_settings():
    # Vérifie le comportement avec un dictionnaire vide.
    assert view_settings({}) == "No settings available.", (
        "La fonction ne détecte pas un dictionnaire vide !"
    )

    # Vérifie l'affichage des paramètres.
    test_config = {"theme": "dark", "volume": "high"}

    assert (
        view_settings(test_config)
        == "Current User Settings:\nTheme: dark\nVolume: high\n"
    ), "La fonction affiche incorrectement les paramètres !"


if __name__ == "__main__":
    # Exécution des tests.
    test_add_setting()
    test_update_setting()
    test_delete_setting()
    test_view_settings()

    print("Tous les tests sont réussis !")
