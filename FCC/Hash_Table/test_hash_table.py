import pytest

from hash_table import HashTable


def test_hash():
    table = HashTable()

    assert table.hash("abc") == 294
    assert table.hash("name") == 417


def test_add():
    table = HashTable()

    table.add("name", "Mathieu")
    table.add("level", "999")

    assert table.lookup("name") == "Mathieu"
    assert table.lookup("level") == "999"


def test_remove():
    table = HashTable()

    table.add("name", "Mathieu")
    table.remove("name")

    assert table.lookup("name") is None


def test_lookup():
    table = HashTable()

    table.add("class", "Guerrier")

    assert table.lookup("class") == "Guerrier"
    assert table.lookup("unknown") is None


def test_collision():
    table = HashTable()

    table.add("abc", "value 1")
    table.add("cba", "value 2")

    assert table.lookup("abc") == "value 1"
    assert table.lookup("cba") == "value 2"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
