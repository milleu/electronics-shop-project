import pytest

from src.item import Item
@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000.0