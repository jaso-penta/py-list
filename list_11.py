# slice notacija
numbers = list(range(21))
# print(numbers)

# numbers_copy = numbers
# print(numbers_copy)

# numbers.append(21)
# print(numbers)
# print(numbers_copy)

# numbers_copy.append(22)
# print(numbers)
# print(numbers_copy)

print()
print('1. nacin')
print()
numbers_copy = numbers.copy()

numbers.append(23)
print(numbers)
print(numbers_copy)

numbers_copy.append(24)
print(numbers)
print(numbers_copy)


print()
print('2. nacin')
print()
numbers_copy = numbers[ : : ]

numbers.append(31)
print(numbers)
print(numbers_copy)

numbers_copy.append(32)
print(numbers)
print(numbers_copy)