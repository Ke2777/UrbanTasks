def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(a = 2, b=45, c=[5, 8, 3])

values_list = [2, 'ghbdtn', True]
values_dict = {'a': 2, 'b': 'aaaaaaaaaaa', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['ghbdtn', True]
print_params(*values_list_2, 42)

