from src.item import Item

class MixinLog:
    language = "EN"
    def __init__(self):
        return self.language

    def change_lang(self):
        """меняет язык с ангийского на русский"""
        if self.language == "EN":
            self.language = "RU"
            return self
        else:
            self.language = "EN"
            return self


class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        """передаем атрибуты класса Item"""
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"