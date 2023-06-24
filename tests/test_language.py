import pytest

from src.keyboard import Keyboard

@pytest.fixture
def kb():
    Keyboard.language = "EN"
    return Keyboard('Dark Project KD87A', 9600, 5)
    return Keyboard.language


def test_init(kb):
    assert kb.name == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    assert kb.price == 9600
    assert kb.quantity == 5



def test_lang_change(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
