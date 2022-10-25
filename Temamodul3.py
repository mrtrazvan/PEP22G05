parola = 7767
while True:
    alegere = int(input("spune mi o parola "))
    if alegere == parola:
        break
        print("Parola gresita , mai incearca:")
print("Acces granted")



cuvant = input("introduceti un cuvant fara majuscule:")
x = cuvant[0]
n = 0

for i in cuvant:
    if i ==x:
        n+=1
print(f"{x} apare de {n} ori")

lista = ["masa",5,"scaun",4.5,[5,6,7],8]
print("Tipul obiectului", lista[0], "este", type(lista[0]))
print("Tipul obiectului", lista[1], "este", type(lista[1]))
print("Tipul obiectului", lista[2], "este", type(lista[2]))
print("Tipul obiectului", lista[3], "este", type(lista[3]))
print("Tipul obiectului", lista[4], "este", type(lista[4]))
print("Tipul obiectului", lista[5], "este", type(lista[1]))










