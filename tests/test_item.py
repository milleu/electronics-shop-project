import pytest

from src.item import Item
from src.phone import Phone
@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)
@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000.0

def test_item_get_all(item):
    item.add_all()
    assert item.all == ["Смартфон", 10000, 20]


def test_instantiate_from_csv():
    item1 = Item("Смартфон", 100, 1)
    item2 = Item("Ноутбук", 1000, 3)
    Item.all = [item1, item2]
    assert len(Item.all) == 2
    assert Item.all[0] == item1
    assert Item.all[1] == item2

def test_string_to_number():
    assert Item.string_to_number('5') == 5
def test_name_too_long_len(item):
    """Название товара слишком длинное"""
    with pytest.raises(Exception):
        item.name = 'ТелефонТелефонТелефон'

def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"

def test_sts(item):
    assert str(item) == 'Смартфон'

def test_add(item, phone):
    assert item + phone == 25
    assert phone + phone == 10