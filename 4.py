"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат
— цена товара со скидкой. Чтобы все работало корректно,
не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


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


class ItemDiscountReport:

    def __init__(self, product: ItemDiscount, discount: float):
        self.product = product
        self.discount = discount / 100

    @property
    def get_parent_data(self):
        return f"Product {self.product.name} has price {self.product.price}"

    def __str__(self):
        return f"Цена товара {self.product.name} с учетом скидки: {round(self.product.price * (1 - self.discount), 2)}."


parent_item = ItemDiscount("PC", 35999.99)
children_item = ItemDiscountReport(parent_item, 15)

print(children_item)
