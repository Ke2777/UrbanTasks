immutable_var = ('Кирилл', 22, True)
print(immutable_var)
immutable_var[2] = False # Изменить immutable_var не получится, это приведет к ошибке компиляции тк элементы кортежа запрещено менять.

mutable_list = ['Кирилл', 22, True]
mutable_list[2] = False
print(mutable_list)