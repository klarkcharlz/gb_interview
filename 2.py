"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы
программы будет сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport:

    def __init__(self, product: ItemDiscount):
        self.product = product

    @property
    def get_parent_data(self):
        return f"Product {self.product.__name} has price {self.product.__price}"


parent_item = ItemDiscount("PC", 35999.99)

# сохранение какой логики ?
# обратиться к атрибутам пока даже не просят
