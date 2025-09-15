# slice notacija
numbers = list(range(21))
print(numbers)

# range(start, stop, step)
# slice je identican samo umjesto naziva range pisemo naziv liste i koristimo [] zagrade,
# a indekse razdvajamo znakom :

# dohvati elemente liste numbers od elementa na indeksu 0 (ukljucivo) 
# do elementa na indeksu 10 (NIJE ukljucen) i uzimi svaki drugi, odnosno korak je 2
sliced_numbers = numbers[ 0 : 10 : 2 ]
print(sliced_numbers)

# korak nije nuzno definirati pa ga mozemo izostaviti, a onda se uzim da je vrijednost koraka 1
sliced_numbers = numbers[ 0 : 10 ]
print(sliced_numbers)


# ako zelimo poceti o zadanjeg elementa liste koristimo negativne vrijednosti.
# ako zelimo uljuciti i zadnji element onda indeks na tom mjesto ustavimo prazan
sliced_numbers = numbers[ 10 : : -1 ]
print(sliced_numbers)

# nova lista s elementima obrnutim redom
sliced_numbers = numbers[ -1 : : -1 ]
print(sliced_numbers)
sliced_numbers = numbers[ : : -1 ]
print(sliced_numbers)


# slice notacija za kopiranje liste
list_copy = numbers[ : : ]
print(list_copy)