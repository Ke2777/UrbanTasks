# Задача 1: Арифметика
result_task1 = 9**0.5 * 5
print(result_task1)

# Задача 2: Логика
result_task2 = 9.99 > 9.98 and 1000 != 1000.1
print(result_task2)

# Задача 3: Школьная загадка
expression_without_priority = 2 * 2 + 2
expression_with_priority = 2 * (2 + 2)
comparison_result = expression_without_priority == expression_with_priority
print(expression_without_priority)
print(expression_with_priority)
print(comparison_result)

# Задача 4: Первый после точки
number_string = '123.456'
number_float = float(number_string)
shifted_number = number_float * 10
first_decimal_digit = int(shifted_number) % 10
print(first_decimal_digit)
