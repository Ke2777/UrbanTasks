word = 'мир'

# 1
example = f"Привет'{word}'"

# 2
print(example[0])

# 3
print(example[-1])

# 4
l = len(example)/2
l -= 1 if l%2 != 0 else None
print(example[int(l):])

# 5
print(example[::-1])

#6
print(example[::2])