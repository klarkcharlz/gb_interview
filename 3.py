"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения,
в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""

keys = ["key1", "key2", "key3", "key4", "key5", "key6"]
values = ["val1", "val2", "val3", "val4"]

# keys = ["key1", "key2", "key3", "key4"]
# values = ["val1", "val2", "val3", "val4", "val5", "val6"]

if len(values) < len(keys):
    values.extend([None for _ in range(len(keys) - len(values))])

print(dict([(key, value) for key, value in zip(keys, values)]))
