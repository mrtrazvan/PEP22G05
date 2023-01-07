nume = input("Cum te numesti?!")
str_note = input("Ce note ai?")
assert str_note , "nu ai dat nicio nota"
note =str_note.split(",")
lista_note = []

for nota in note:
    try:
        lista_note.append(int(nota))
    except ValueError:
        print("introduceti note 1-10")

media = sum(lista_note)/len(lista_note)
print("Media este:" , media)
if media>= 5:
    print(f"{nume} a trecut clasa")
else:
    print(f"{nume} nu a trecut calsa")
print(lista_note)
