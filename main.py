# Implementing various Cryptography Algorithms

import pycryptographyalgos as crypto


text = "PES University"
print("Text: ",text)
print()

print("*******************")
print("1. Caesar Cipher")
shift = 4
print("Shift:",shift)
cipher = crypto.caesar.encrypt(text, shift)
print("Encrypted Text: ", cipher)
decrypt_text = crypto.caesar.decrypt(cipher, shift)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()

print("*******************")
print("2. Transposition Cipher")
key = 3
print("Key:", key)
cipher = crypto.transposition.encrypt(text, key)
print("Encrypted Text: ", cipher)
decrypt_text = crypto.transposition.decrypt(cipher, key)
print("Decrypted Text: ", decrypt_text)
print("*******************")
print()