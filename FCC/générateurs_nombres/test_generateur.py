import pytest

from generateur import range_of_numbers


def test_range_of_numbers():
    (
        range_of_numbers(1, 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "l'iteration de la fonction a un probléme",
    )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
