import random

field_1 = random.randint(3, 20)
field_2 = []
print(field_1)

pare_list = []
for i in range(1, field_1):
    pare = [i, 0]
    for j in range(i + 1, field_1):
        pare[1] = j
        pare_list.append(pare.copy())

for i in pare_list:
    pare_sum = sum(i)
    if field_1 % pare_sum == 0:
        field_2.append(i)

formatted_output = ''.join(f'{x[0]}{x[1]}' for x in field_2)
print(formatted_output)
