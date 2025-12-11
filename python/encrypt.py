# program for encrypting message in python

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars :{chars}")
print()
print(f"key :{key}")

#for ENCRYPT

plain_text = input("Enter a message to be encrypted :")
cipher_text = ""

for letter in plain_text :
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message :{plain_text}")
print(f"encrypted message :{cipher_text}")