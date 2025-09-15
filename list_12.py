import math

sqrt_numbers = [] # kvadrati brojeva od 1 do 20
print(sqrt_numbers)

for number in range(1, 21):
    # sqrt_numbers.append(number * number)
    sqrt_number = number ** 2
    sqrt_numbers.append(sqrt_number)
    # sqrt_numbers.append(number ** 2)
    # sqrt_numbers.append(math.sqrt(number))


print(sqrt_numbers)



# cisto napisani kod
sqrt_numbers = []

for number in range(1, 21):
    sqrt_numbers.append(number ** 2)



# jos kraci nacin zapisa gornjeg rjesenja
# ili list comprehesion
# sqrt_numbers = [number ** 2 for number in range(1, 21)]
# jos krace
sqrt_numbers = [x ** 2 for x in range(1, 21)]
print(sqrt_numbers)