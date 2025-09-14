import random


languages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']

movies = ['Memento', 'Dark Knight', 'Seven', 'Coach Carter', 'Dead poet society', 'In to the wild', 'Lost in 60 seconds']

football_clubs = ['Chelsea', 'Arsenal', 'Manchaster City', 'Manchaster United', 'West Ham', 'Tottenham', 'Liverpool']



while True:
    
    selected_topic = input('\nIzaberi temu: Jezik; Filmovi; Sport\n(Za izlazak iz aplikacije: exit):\n')

    if selected_topic == 'exit':
        print('\nPozdrav, do sljedeceg puta !\n')
        break

    # Biranje teme
    if selected_topic == 'jezik':
        print('Izabrali ste temu Programski jezik')
        topic_list = languages[:]
        theme = 'Jezik'

    elif selected_topic == 'filmovi':
        print('Izabrali ste temu Filmovi')
        topic_list = movies[:]
        theme = 'Film'

    elif selected_topic == 'sport':
        print('Izabrali ste temu Sport')
        topic_list = football_clubs[:]
        theme = 'Engleski nogometni klub'

    else:
        print('Nepostojeca tema, pokusajte ponovno')
        continue

    # IGRA
    while True:
        counter = 0
        selected_index = random.randint(0, len(topic_list) - 1)
        print(selected_index)
        guess = input(f'\nPogodi {theme}:\n').lower()
        counter += 1

        if guess.lower() == topic_list[selected_index].lower():
            print(f'\nCestitmo! pogodili ste iz {counter} pokusaja')

        else:
            print(f'\nNazalost niste pogodili {theme}')

        while True:
            new_game = input('Zelite li novu igru? (Da/Ne)\n')
            if new_game == 'da':
                conuter = 0
                selected_index = random.randint(0, len(topic_list) - 1)
                break
            elif new_game == 'ne':
                print('\nPovratak na selekciju tema.\n')
                break
            else:
                print('\nError, molim odgovor Da ili Ne')
                continue
        if new_game == 'ne':
            break
        