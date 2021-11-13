"""
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский,
и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция, отвечающая за отображение информации о товаре
в одной строке).
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

    def __init__(self, product: ItemDiscount):
        self.product = product

    @property
    def get_parent_data(self):
        return f"Product {self.product.name} has price {self.product.price}"


parent_item = ItemDiscount("PC", 35999.99)
children_item = ItemDiscountReport(parent_item)

print(children_item.get_parent_data)

parent_item.name = "SSD"
parent_item.price = 199.99

print(children_item.get_parent_data)
