"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
"""
from abc import ABC, abstractmethod


class ItemDiscount:

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __get_name(self):
        return self.__name

    def __get_price(self):
        return self.__price

    def __set_name(self, name):
        self.__name = name

    def __set_price(self, price):
        self.__price = price

    name = property(__get_name, __set_name)
    price = property(__get_price, __set_price)


class ItemDiscountReport(ABC):

    def __init__(self, product: ItemDiscount):
        self.product = product

    @abstractmethod
    def get_info(self):
        pass


class ItemDiscountReportPrice(ItemDiscountReport):

    def __init__(self, product: ItemDiscount):
        super().__init__(product)

    @property
    def get_info(self):
        return self.product.price


class ItemDiscountReportName(ItemDiscountReport):

    def __init__(self, product: ItemDiscount):
        super().__init__(product)

    @property
    def get_info(self):
        return self.product.name


parent_item = ItemDiscount("PC", 35999.99)
children_item_price = ItemDiscountReportPrice(parent_item)
children_item_name = ItemDiscountReportName(parent_item)

print(children_item_price.get_info)
print(children_item_name.get_info)


# тут уже логично помоему сделать родительский класс для репорта
# и сделать его абстрактным обязав переопределить get_info
