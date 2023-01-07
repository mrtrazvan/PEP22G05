# binary chars
# 10 = 0000 1010
# 10 = 0    A

a_number = ord("a")
A_number = ord("A")

print(bin(A_number))
print(bin(a_number))

print(max("abcdZ!"))

letter1 = chr(70)
letter2 = chr(33)

print(letter1, letter2)
print(10 *"*")

my_message = "This is my message"
encrypted_result = ""

for letter in my_message:
    encrypted_result +=chr(ord(letter)^48)

print(encrypted_result)

decrypted_result = ""

for letter in encrypted_result:
    decrypted_result+=chr(ord(letter)^48)
print(decrypted_result)

print(ord("c"))

numar = input("")
print(numar)