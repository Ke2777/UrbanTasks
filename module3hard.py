def calculate_structure_sum(*data, result=0):
    for i in data:
        if isinstance(i, str):
            result += len(i)
        elif isinstance(i, int):
            result += i
        elif isinstance(i, dict):
            result = calculate_structure_sum(*list(i.keys()), result=result)
            result = calculate_structure_sum(*list(i.values()), result=result)
        else:
            result = calculate_structure_sum(*i, result=result)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
