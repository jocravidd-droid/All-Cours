from annuaire_telephonique.py import ajouter_contact, info, rechercher_contact


def test_ajouter_contact():
    info.clear()

    ajouter_contact("Lucas", 612345678)

    assert "Lucas" in info
    assert info["Lucas"] == 612345678


def test_rechercher_contact():
    info.clear()

    ajouter_contact("Lucas", 612345678)

    assert rechercher_contact("Lucas") == 612345678
