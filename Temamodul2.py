parola = "Pass1me"
parola1 = input("spune o parola")
print(parola ==parola1)


nume = input("Introduceti un nume de referinta")
prenume = input("Introduceti alt nume")
print("Lungimea primului nume este: " , len(nume))
print("Numele de referinta este mai lung decat numele dat: ", len(nume) > len(prenume))
print("Initiala numelui de referinta este: " ,nume[0])
text = nume[::-1]
print("Numele de referinta inversat este: " ,text)
numar = int(input("Introduceti un numar"))
print(3*nume)



cuvant = input("spune un cuvant")
print(cuvant.lower() == cuvant.lower()[::-1])

x = "a\nn\na\nn\na\ns\n"
print(x)


x = "Ananas"
print(x[0:3])
print(x[3:])

print(x[0:2],x[2:5],x[5],sep=":")

print(x[0:3],x[3:5],x[5],sep="_")
print(x[1:3]*8)

cuvant = input("Spune un cuvant")
print("Sirul incepe cu majuscula ", cuvant[0]==cuvant.upper()[0])

