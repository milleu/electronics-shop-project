import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self ) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * self.pay_rate


    def add_all(self):
        self.all.append(self.__name)
        self.all.append(self.price)
        self.all.append(self.quantity)
        return all
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, item_name: str):
        if len(item_name) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = item_name
    @classmethod
    def instantiate_from_csv(csl):
        with open("../src/items.csv", newline="") as file:
            reader = csv.reader(file)
            for string in reader:
                if string[0] != "name":
                    __name, price, quantity = string[0], string[1], string[2]
                    item1 = Item(__name, price, quantity)
                    csl.all.append(item1)

    def __repr__(self) ->str:
        return f"Item(name='{self.name}', price='{self.price}, quantity='{self.quantity}')"
    @staticmethod
    def string_to_number(string: str):
        """статический метод, возвращающий число из числа-строки"""
        num = float(string)
        int_num = int(num)
        return int_num





