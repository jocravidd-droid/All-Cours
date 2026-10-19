from qcm import extraire_choix, charger_qcm


def test_extraire_choix():
    resultat = extraire_choix("Question A-1 B-4 C-8")
    assert resultat == ["A", "B", "C"]


def test_charger_qcm():
    resultat = charger_qcm("qcm.txt", [], {})
    assert isinstance(resultat, dict)
    assert len(resultat) >= 10


test_extraire_choix()
test_charger_qcm()

print("Tests réussis !")
