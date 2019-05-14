# Transposition Cipher
# Make a 'key'x'key' matrix and write the word. now take transpose of the matrix and join together.
import math


def encrypt(text,key):
    columns = [''] * key
    for pos, c in enumerate(text):
        columns[pos % 3] += c
    return ''.join(columns)


def decrypt(text, key):
    num_of_columns = math.ceil(len(text) / key)
    columns = [''] * num_of_columns

    for pos, c in enumerate(text):
        columns[pos % num_of_columns] += c
    return ''.join(columns)
