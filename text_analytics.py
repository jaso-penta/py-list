# Zadatak u varijabli text pronadite koliko se pita pojavljuje neka rijec, recimo lorem.
# Ispisati statistiku poijavljivanja pojedinih rijeci
text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Vivamus molestie ligula vehicula, vehicula erat a, ultrices mauris. 
Cras semper ex vel egestas blandit. Fusce faucibus hendrerit ante sit amet tristique. 
Quisque venenatis metus quis dignissim lacinia. Donec sodales eget elit id sodales. 
Donec nunc justo, ornare quis est ut, accumsan vestibulum sem. 
Integer sollicitudin dapibus ullamcorper. 
Fusce tincidunt, sapien non dictum sagittis, ligula ligula pulvinar purus, 
tempus porttitor ante risus quis ante. Aenean quis orci fermentum, bibendum neque quis, sollicitudin neque. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Vestibulum lacinia lacus vel lacus accumsan semper. 
Duis eu purus ultrices, convallis massa in, pulvinar metus. 
Etiam placerat, elit sit amet porta auctor, magna felis accumsan ipsum, 
eget scelerisque augue dolor ultrices nisl. Curabitur id sollicitudin sem.
'''
# occurrences = text.count('semper')

# print(f'Rijec Lorem se pojavljuje {occurrences} puta u tekstu.')

# statistika ponavljanja rijeci
words = text.split()
cleaned_text = []

# u ovim for petljama za svaku rijec prvojeriti koliko se puta pojavljuje u teksu ili listi i ispisati to u konzolu
for word in words:
    # 1. korak pripremiti podatke za analizu
    word = word.lower()
    word = word.strip()
    word = word.replace('.', '')
    word = word.replace(',', '')

    cleaned_text.append(word)


for word in cleaned_text:
    # 2. korak obraditi podatke
    word_occurrences = cleaned_text.count(word)

    print(f'Rijec {word} se ponavlja {word_occurrences} puta.')