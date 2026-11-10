import pytest

from app_budget import Category, create_spend_chart


def test_create_spend_chart():
    food = Category("Food")
    clothing = Category("Clothing")

    food.deposit(100)
    clothing.deposit(100)

    food.withdraw(30, "Groceries")
    clothing.withdraw(10, "Shirt")

    chart = create_spend_chart([food, clothing])

    assert chart.startswith("Percentage spent by category\n")
    assert " 70| o     \n" in chart
    assert " 20| o  o  \n" in chart


if __name__ == "__main__":
    pytest.main(["-v", __file__])
