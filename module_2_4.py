numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:  # Цикл для перебора элементов списка.
    is_prime = True
    for j in range(2, i):  # Цикл для поиска составных чисел
        if i % j == 0:
            is_prime = False

    if i != 0 and i != 1:
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)


print(primes)
print(not_primes)
