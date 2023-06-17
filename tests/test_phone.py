import pytest

from src.phone import Phone

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0

def test_init(phone):
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2
