"""
Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ItemDiscountReport:

    def __init__(self, product: ItemDiscount):
        self.product = product

    @property
    def get_parent_data(self):
        return f"Product {self.product.__name} has price {self.product.__price}"


parent_item = ItemDiscount("PC", 35999.99)


# не понял и не стал делать ItemDiscountReport дочерним
# его задача только возвращать цену и имя товара одной строкой
# зачем ему остальные атрибуты родителя нужны
# ему нужен только метод get_parent_data
# проще и логичнее при инициализации передвать обьект класса из которого будем брать данные
