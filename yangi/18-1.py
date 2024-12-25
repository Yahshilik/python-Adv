
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

    def __gt__(self, other:"Computer"):
        return self.__price > other.price



class Monoblok(Computer):
    def __init__(self, brend, model, year, price, scrn_size):
        super().__init__(brend, model, year, price)
        self.scrn_size = scrn_size

    def display_info(self):
        return f"{self.model} - {self.scrn_size} : {self.price}"


class Notebook(Computer):
    def __init__(self, brend, model, year, price, scrn_size, battery_life):
        super().__init__(brend, model, year, price)
        self.battery_life = battery_life
        self.scrn_size = scrn_size

    def display_info(self):
        return f"{self.model} - {self.battery_life} : {self.price}"

class Factory:
    factory_count=0
    def __init__(self):
        self.item = []

    @classmethod
    def get_items(cls):
        return cls.factory_count

    def add_product(self,value):
        if isinstance(value, Computer):
            self.item.append(value)
            print(f"{value.display_info()} qushildi")
            return
        else:
            print("Xato kiritildi")



notebook1 = Notebook("Acer", "A15", 2024, "200$", "15.4", "5h")
notebook2 = Notebook("Dell", "d1", 2024, "250$", "15.4", "5h")
monoblok1 = Monoblok("HP", "HP24", 2024, "240$", "24")
monoblok2 = Monoblok("Acer", "A24", 2024, "220$", "24")

print(notebook1.display_info())
print(monoblok1.display_info())
