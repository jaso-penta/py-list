# Dodati brojac pokusaja te prilagoditi ispis nakon sto korisnik pogodi tako da napise koliko pokusaja je pogodio naziv programskog jezika

# import - ovo cemo uskoro raditi
import random


# deklaracija pocetnih vrijednosti
languages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']
selected_language_index = random.randint(0, 7)
print(languages[selected_language_index])


# glavni dio programa
while True:
    user_guess = input('Pogodite naziv programskog jezika: ')

    if user_guess.lower() == languages[selected_language_index].lower():
        print('Cestittamo!! Pogodili ste naziv programskog jezika')
        break
    else:
        print('Na zalost niste pogodili. Pokusajte ponovno')



    next_round = input('Zelite li nastaviti? (Da/Ne): ')
    if next_round == 'ne':
        break

# zavrsetak aplikacije
print()
print('Hvala i dovidjenja')