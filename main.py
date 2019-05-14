# Implementing various Cryptography Algorithms

from pycryptographyalgos import *


text = "PES University"

print("Text: ",text)
print()

print("*******************")
print("1. Caesar Cipher")
shift = 4
print("Shift:",shift)
cipher = caesar_cipher.encrypt(text, shift)
print("Encrypted Text: ", cipher)
decrypt_text = caesar_cipher.decrypt(cipher, shift)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("2. Transposition Cipher")
key = 3
print("Key:", key)
cipher = transposition_cipher.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = transposition_cipher.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("3. Vigenere Cipher")
key = "SECRETKEY"
print("Key:", key)
cipher = vigenere_cipher.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = vigenere_cipher.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("4. Multiplicative Cipher")
key = 7
print("Key:", key)
cipher = multiplicative_cipher.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = multiplicative_cipher.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("5. Affine Cipher")
key = (7, 3)
print("Key:", key)
cipher = affine_cipher.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = affine_cipher.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()