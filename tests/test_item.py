import pytest

from src.item import Item

def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000

def test_apply_discount():
    assert Item("Смартфон", 10000, 20).apply_discount(0.8) == 8000.0