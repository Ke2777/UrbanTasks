# 1
result = 7 > 5 & 7 < 10
print(result)

# 2
input = int(input('Введите число: '))
result = input % 2 == 0
print(result)

# 3
# 4th program
num_1 = 456
num_2 = 789

mid_num_1 = (num_1//10) % 10
mid_num_2 = (num_2//10) % 10
result = mid_num_1 * mid_num_2
print(result)

# 4
num_1 = 123
num_2 = 456
f_num_1 = num_1 // 100
f_num_2 = num_2 // 100
result = f_num_1 + f_num_2
print(result)

# 5
num_1 = 7.89
num_2 = 89.7
num_3 = 9.87
int_num_1 = int(num_1)
int_num_2 = int(num_2)
int_num_3 = int(num_3)
dec_num_1 = (num_1 * 100) % 100
dec_num_2 = (num_2 * 100) % 100
dec_num_3 = (num_3 * 100) % 100
result = (int_num_1 == dec_num_2 or int_num_1 == dec_num_3 or
          int_num_2 == dec_num_1 or int_num_2 == dec_num_3 or
          int_num_3 == dec_num_1 or int_num_3 == dec_num_2)
print(result)

# 6
print(25 % 7 == 0)