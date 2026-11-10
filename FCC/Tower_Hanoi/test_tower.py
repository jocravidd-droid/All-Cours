import pytest

from tower import hanoi_solver


def test_hanoi_solver():
    result = hanoi_solver(3).split("\n")

    # Vérifie l'état initial
    assert result[0] == "[3, 2, 1] [] []"

    # Vérifie l'état final
    assert result[-1] == "[] [] [3, 2, 1]"

    # Vérifie le nombre total d'états (7 déplacements + état initial)
    assert len(result) == 2**3


def test_hanoi_one_disk():
    assert hanoi_solver(1) == "[1] [] []\n[] [] [1]"


def test_hanoi_zero_disks():
    assert hanoi_solver(0) == "[] [] []"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
