import pytest

from caesar import decrypt, encrypt

texte = "Test de mon chiffrage"


def test_decrypt():
    assert decrypt(text="Cnbc mn vxw lqrooajpn", shift=9) == texte, (
        "la fonction de décryptage marche pas"
    )


def test_encrypt():
    assert encrypt(text=texte, shift=9) == "Cnbc mn vxw lqrooajpn", (
        "la fonction de cryptage ne marche pas"
    )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
