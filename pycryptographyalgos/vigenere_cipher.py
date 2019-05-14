# Vigenere Cipher
# Each letter shifted by a letter by a position down the alphabet corresponding to a letter in the key


def encrypt(text, key):
    encrypted_txt = ""

    for i, c in enumerate(text):
        if c == ' ':
            encrypted_txt += ' '
        elif c.isupper():
            shift = ord(key[i % len(key)])-65
            new_pos = (ord(c) - 65 + shift) % 26
            encrypted_txt += chr(new_pos + 65)
        else:
            shift = ord(key[i % len(key)])-97
            new_pos = (ord(c) - 97 + shift) % 26
            encrypted_txt += chr(new_pos + 97)
    return encrypted_txt


def decrypt(text, key):
    decrypted_txt = ""
    for i, c in enumerate(text):
        if c == ' ':
            decrypted_txt += ' '
        elif c.isupper():
            shift = ord(key[i % len(key)]) - 65
            new_pos = (ord(c) - 65 - shift) % 26
            decrypted_txt += chr(new_pos + 65)
        else:
            shift = ord(key[i % len(key)]) - 97
            new_pos = (ord(c) - 97 - shift) % 26
            decrypted_txt += chr(new_pos + 97)
    return decrypted_txt