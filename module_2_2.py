first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
result = 0

if first == second == third: result = 3
else:
    if first == second: result += 2
    if second == third: result += 2
    if third == first: result += 2

print(result)