# Transposition Cipher
# Make a 'key' column matrix and write the word. now take each column and join together to make encrypted string
import math


def encrypt(text,key):
    columns = [''] * key
    for pos, c in enumerate(text):
        columns[pos % 3] += c
    return ''.join(columns)


def decrypt(text, key):
    num_of_columns = math.ceil(len(text) / key)
    num_of_rows = key
    num_of_blank = num_of_columns*key - len(text)

    columns = [''] * num_of_columns

    curr_col = 0
    curr_row = 0
    for pos, c in enumerate(text):
        # if we've exceeded max columns, or if there's a blank in the last column, move to next row
        if curr_col == num_of_columns or (curr_col == num_of_columns-1 and curr_row >= num_of_rows-num_of_blank):
            curr_col = 0
            curr_row += 1

        columns[curr_col] += c
        curr_col += 1

    return ''.join(columns)
