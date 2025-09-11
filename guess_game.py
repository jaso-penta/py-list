# ZADATAK dio 1. dodati mogucnost izbora teme pogadanja naziva:
# teme mogu biti proizvoljne, a evo primjera: filmovi, sport, slavne osobe, mitologija ...
# HINT - za svaku temu kreirajte kolekciju i ovisno o izboru izvucite nasumicno jednog clana te kolekcije

# Ako zelite dodajte i hint korisniku tako da mu prikazete prvo slovo naziva kojeg pogada, ALI nakon treceg pokusaja!!!

# import - ovoe cemo uskoro raditi, ali za sada zanemriti
import random


# deklaracija pocetnih vrijednosti
languages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']
selected_language_index = random.randint(0, 7)
counter = 0
print(languages[selected_language_index])


# glavni dio aplikacije
while True:
    users_guess = input('Pogodite naziv programskog jezika: ')
    counter += 1

    if users_guess.lower() == languages[selected_language_index].lower():
        print(f'Cestitamo!!! Pogodili ste naziv programskog jezika iz {counter}. puta!!!')
        # ZADATAK dio 2 - pitati korisnika zeli li npvu igru, ako da reset i nova igra (NEMA upita za next_round!!!),
        # a ako ne onda izaci iz igre.

        selected_language_index = random.randint(0, 7)
        counter = 0
        # break
    else:
        print('Na zalost niste pogodili! Pokusajte ponovno.')



    next_round = input('Zelite li pokusati ponovno? (Da/Ne): ')
    if next_round == 'ne':
        break


# zavrsetak aplikacije
print()
print('Pozdrav, do slijedeceg puta!')
print()