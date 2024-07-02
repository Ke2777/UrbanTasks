# 1
my_dict = {'Пожарная': 111, 'Скорая': 112, 'Полиция': 113, 'Город': 'Санкт-Петербург'}
print(my_dict)
print(my_dict['Город'])
my_dict.update({'Имя': 'Кирилл',
                'Дом': 1})
print(my_dict.pop('Пожарная'))
print(my_dict)

# 2
my_set = {25, 26, 27, True, 'City', True, False, 24, 24}
print(my_set)
my_set.update({23, 22})
my_set.remove(True)
print(my_set)


