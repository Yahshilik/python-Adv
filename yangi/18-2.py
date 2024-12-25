
from abc import ABC, abstractmethod

class Computer:
    total_com = 0
    def __init__(self, brend, model, year, price):
        self.brend = brend
        self.model = model
        self.year = year
        self.__price = price
        Computer.total_com += 1

    @classmethod
    def get_items(cls):
        return cls.total_com

    @abstractmethod
    def display_info(self):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class Monoblok(Computer):
    def __init__(self, brend, model, year, price, scrn_size):
        super().__init__(brend, model, year, price)
        self.scrn_size = scrn_size

    def display_info(self):
        return f"{self.model} - {self.scrn_size} : {self.price}"

class Notebook(Computer):
    def __init__(self, brend, model, year, price, battery_life):
        super().__init__(brend, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return f"{self.model} - {self.battery_life} : {self.price}"

class Factory:
    factory_count = 0
    def __init__(self):
        self.item = []

    @classmethod
    def get_items(cls):
        return cls.factory_count

    def add_product(self, value):
        if isinstance(value, Computer):
            self.item.append(value)
            print(f"{value.display_info()} qoshildi")
            return
        else:
            print("Xato kiritildi")

notebook1 = Notebook("Acer", "A15", 2024, "250$", "5-5hr")
notebook2 = Notebook("Dell", "D3", 2024, "280$", "6hr")
monoblok1 = Monoblok("Lenovo", "Slim", 2024, "300$", "22")
monoblok2 = Monoblok("AvTech", "X1" , 2024, "250$", "24")


print(notebook1.display_info())
print(monoblok2.display_info())
