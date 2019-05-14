# Library of Cyptography Algorithms


# Caesar Cipher
# Each letter replaced by a letter with 's' positions down the alphabet.

def caesar_cipher(text, s):
    encrypted_txt = ""
    for c in text:
        if c.isupper():
            new_pos = (ord(c) - 65 + s) % 26 + 65
            encrypted_txt += chr(new_pos)
        else:
            new_pos = (ord(c) - 97 + s) % 26 + 97
            encrypted_txt += chr(new_pos)
    return encrypted_txt

text = "PES University"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + caesar_cipher(text, s))