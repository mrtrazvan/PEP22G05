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