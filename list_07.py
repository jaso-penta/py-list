# sortiranje elemenata liste
bands = [
    'The Beatles',
    'Pink Floyd',
    'Queen',
    'Nirvana',
    'Radiohead',
    'Metallica',
    'Coldplay'
]
print('Lista prije sorted', bands)
print()

# funkcija ne mijenja listu i sortira elemente od manjeg prema vecem
for band in sorted(bands):
    print(band)

print()
print('Lista poslije sorted', bands)

# funkcija ne mijenja listu i sortira elemente od veceg prema manjem
for band in sorted(bands, reverse=True):
    print(band)

print()
print('Lista poslije sorted reverse', bands)


# sortira listu od manjeg prema vecem i trajno mijenja vrijednost varijable u kojoj je pohranjena lista
bands.sort()
print()
print('Lista poslije sort metode', bands)

# sortira listu od veceg prema manjem i trajno mijenja vrijednost varijable u kojoj je pohranjena lista
bands.sort(reverse=True)
print()
print('Lista poslije sort(reverse=True) metode', bands)