# okretanje elemenata liste od zadnjeg prema prvom
bands = [
    'The Beatles',
    'Pink Floyd',
    'Queen',
    'Nirvana',
    'Radiohead',
    'Metallica',
    'Coldplay'
]
print('Lista prije reversed', bands)
print()

# funkcija ne mijenja listu i sortira elemente od manjeg prema vecem
for band in reversed(bands):
    print(band)

print()
print('Lista poslije reversed', bands)


# sortira listu od manjeg prema vecem i trajno mijenja vrijednost varijable u kojoj je pohranjena lista
bands.reverse()
print()
print('Lista poslije reverse metode', bands)