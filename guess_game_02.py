import random


# deklaracija pocetnih vrijednosti
languages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']
selected_language_index = random.randint(0, 7)

movies = ['Memento', 'Dark Knight', 'Seven', 'Coach Carter', 'Dead poet society', 'In to the wild', 'Lost in 60 seconds']
selected_movies_index = random.randint(0, 7)

football_clubs = ['Chelsea', 'Arsenal', 'Manchaster City', 'Manchaster United', 'West Ham', 'Tottenham', 'Liverpool']
selected_football_clubs_index = random.randint(0, 7)



counter = 0


# Main dio aplikacije
while True:

    selected_topic = input('Izaberi temu: jezici, filmovi, sport: ')

    
    if selected_topic.lower() == 'jezici'.lower():
        print('Izabrali ste temu Programski jezici ')
        
        while True:
            guess_language = input('Izaberite programski jezik: ')
            counter += 1

            if guess_language.lower() == languages[selected_language_index].lower():
                print(f'Cestitam, pogodili ste jezik iz {counter} puta! ')
                selected_language_index = random.randint(0, 7)
                counter = 0

                new_guess = input('Zelite li novu igru ? (Da/Ne): ')
                if new_guess == 'ne'.lower():  
                    break
                    
            
            else:
                print('Na zalost niste pogodili jezik ')
                new_guess = input('Zelite li novu igru ? (Da/Ne): ')
                if new_guess == 'ne'.lower():  
                    break
                    



    elif selected_topic.lower() == 'filmovi'.lower():
        print('Izabrali ste temu Filmovi ')
        guess_movie = input('Izaberite film: ')
        counter += 1

        if guess_movie.lower() == movies[selected_movies_index].lower():
            print(f'Cestitamo, pogodili ste film iz {counter} pokusaja! ')
            
            counter = 0
        
        else:
            print('Na zalost niste pogodili film')


    elif selected_topic.lower() == 'sport'.lower():
        print('Izabrali ste temu Sport ')
        guess_club = input('Izaberite engleski klub: ')
        counter += 1

        if guess_club.lower() == football_clubs[selected_football_clubs_index].lower():
            print(f'Cestitamo, pogodili ste klub iz {counter} pokusaja! ')
            
            counter = 0
        
        else:
            print('Na zalost niste pogodili klub')


    if new_guess == 'ne':
        print('Pozdrav do sljedeceg puta')
        break

    next_round = input('Zelite li pokusati ponovno? (Da/Ne): ')
    if next_round == 'ne':
        break





    # Zavrsetak aplikacije
    print()
    print('Pozdrav do sljedeceg puta! ')
    print()
