# Implementing various Cryptography Algorithms

from pycryptographyalgos import *


text = "PES University"

print("Text: ",text)
print()

print("*******************")
print("1. Caesar Cipher")
shift = 4
print("Shift:",shift)
cipher = caesar.encrypt(text, shift)
print("Encrypted Text: ", cipher)
decrypt_text = caesar.decrypt(cipher, shift)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("2. Transposition Cipher")
key = 3
print("Key:", key)
cipher = transposition.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = transposition.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("3. Vigenere Cipher")
key = "SECRETKEY"
print("Key:", key)
cipher = vigenere.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = vigenere.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()