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

    selected_topic = input('\nIzaberi temu: Jezici; Filmovi; Sport\n(Za izlazak iz aplikacije: exit):\n')

    if selected_topic == 'exit':
        print('\nPozdrav, do sljedeceg puta !\n')
        break

    
    if selected_topic.lower() == 'jezici'.lower():
        print('\nIzabrali ste temu Programski jezici ')
        
        while True:
            guess_language = input('Izaberite programski jezik: ')
            counter += 1

            if guess_language.lower() == languages[selected_language_index].lower():
                print(f'Cestitam, pogodili ste jezik iz {counter} puta! ')
                selected_language_index = random.randint(0, 7)
                counter = 0
                
                exit_topic = False
                while True:
                    new_game = input('Zelite li novu igru ? (Da/Ne): ')
                    if new_game == 'ne'.lower():  
                        print('\nPovratak na selekciju tema\n')
                        exit_topic = True
                        break
                    elif new_game == 'da'.lower():
                        break
                    else:
                        print('Error, molimo unesite da ili ne')
                
                if exit_topic:
                    break

            
                    
            else:
                print('Na zalost niste pogodili jezik ')
                
                while True:
                    new_game = input('Zelite li novu igru ? (Da/Ne): ')
                    if new_game == 'ne'.lower():  
                        print('\nPovratak na selekciju tema\n')
                        exit_topic = True
                        break
                    elif new_game == 'da'.lower():
                        break
                    else:
                        print('Error, molimo unesite da ili ne')

                if exit_topic:
                    break
                 

                    
    elif selected_topic.lower() == 'filmovi'.lower():
        print('Izabrali ste temu Filmovi ')

        while True:
            guess_movie = input('Izaberite film: ')
            counter += 1

            if guess_movie.lower() == movies[selected_movies_index].lower():
                print(f'Cestitamo, pogodili ste film iz {counter} pokusaja! ')
                selected_movies_index = random.randint(0, 7)
                counter = 0

                exit_topic = False
                while True:
                    new_game = input('Zelite li novu igru ? (Da/Ne): ')
                    if new_game == 'ne'.lower():  
                        print('\nPovratak na selekciju tema\n')
                        exit_topic = True
                        break
                    elif new_game == 'da'.lower():
                        break
                    else:
                        print('Error, molimo unesite da ili ne')
                    
                if exit_topic:
                    break



            else:
                print('Na zalost niste pogodili film')
                
                while True:
                    new_game = input('Zelite li novu igru ? (Da/Ne): ')
                    if new_game == 'ne'.lower(): 
                        print('\nPovratak na selekciju tema\n')
                        exit_topic = True 
                        break
                    elif new_game == 'da'.lower():
                        break
                    else:
                        print('Error, molimo unesite da ili ne')
                    
                if exit_topic:
                    break


    elif selected_topic.lower() == 'sport'.lower():
        print('Izabrali ste temu Sport ')

        while True:
            guess_club = input('Izaberite engleski klub: ')
            counter += 1

            if guess_club.lower() == football_clubs[selected_football_clubs_index].lower():
                print(f'Cestitamo, pogodili ste klub iz {counter} pokusaja! ')
                selected_football_clubs_index = random.randint(0, 7)
                counter = 0

                exit_topic = True
                while True:
                    new_game = input('Zelite li novu igru ? (Da/Ne): ')
                    if new_game == 'ne'.lower():  
                        exit_topic = True
                        print('\nPovratak na selekciju tema\n')
                        break
                    elif new_game == 'da'.lower():
                        break
                    else:
                        print('Error, molimo unesite da ili ne')
                    
                if exit_topic:
                    break
            
            else:
                print('Na zalost niste pogodili klub')

                exit_topic = True
                while True:
                    new_game = input('Zelite li novu igru ? (Da/Ne): ')
                    if new_game == 'ne'.lower():  
                        print('\nPovratak na selekciju tema\n')
                        exit_topic = True
                        break
                    elif new_game == 'da'.lower():
                        break
                    else:
                        print('Error, molimo unesite da ili ne')
                    
                if exit_topic:
                    break





