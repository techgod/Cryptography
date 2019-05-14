# Affine Cipher
# Combination of Caesar and Affine
# Each letter replaced by a letter with a 'key[1]' times itself + key[0] shift positions down the alphabet.

# Care has to be taken to choose a key such that gcd(key,26)=1 otherwise


def encrypt(text, key):
    encrypted_txt = ""
    for c in text:
        if c == ' ':
            encrypted_txt += ' '
        elif c.isupper():
            new_pos = ((ord(c) - 65) * key[0] + key[1]) % 26
            encrypted_txt += chr(new_pos+65)
        else:
            new_pos = ((ord(c) - 97) * key[0] + key[1]) % 26
            encrypted_txt += chr(new_pos + 97)
    return encrypted_txt


# Extended Euclid's Algorithm
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


# Find Multiplicative inverse
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def decrypt(text, key):
    decrypted_txt=''
    minv = modinv(key[0], 26)
    for c in text:
        if c == ' ':
            decrypted_txt += ' '
        elif c.isupper():
            new_pos = (((ord(c) - 65) - key[1]) * minv) % 26
            decrypted_txt += chr(new_pos + 65)
        else:
            new_pos = (((ord(c) - 97) - key[1]) * minv) % 26
            decrypted_txt += chr(new_pos + 97)
    return decrypted_txt