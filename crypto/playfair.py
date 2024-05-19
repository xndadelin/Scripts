"""
┌──(xndadelin㉿kali)-[~]
└─$ nc mercury.picoctf.net 33686
Here is the alphabet: v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp
Here is the encrypted message: 4celvfdkoq5a0dx7pr40ifzctd8488
What is the plaintext message? ^C
"""
# playfair cipher
from pwn import *
import re
r = remote("mercury.picoctf.net", 33686)
received = r.recvuntil("What is the plaintext message? ")
alphabet, encrypted = re.findall(r"Here is the alphabet: ([a-z0-9]+)\nHere is the encrypted message: ([a-z0-9]+)", received.decode())[0]
alphabet = alphabet.upper()
encrypted = encrypted.upper()
def decode_playfair(alphabet, cipher):
    # Generate the key square
    key_square = []
    for char in alphabet:
        if char not in key_square and char != 'J':
            key_square.append(char)

    # Insert the remaining characters of the alphabet
    for char in alphabet:
        if char not in key_square and char != 'J':
            key_square.append(char)

    # Prepare the key square as a 5x5 grid
    key_matrix = [key_square[i:i+5] for i in range(0, 25, 5)]

    # Remove whitespace and convert to uppercase
    cipher = cipher.replace(" ", "").upper()

    # Replace 'J' with 'I' in the cipher
    cipher = cipher.replace('J', 'I')

    # Split the cipher into pairs of characters
    pairs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]

    # Decode each pair of characters
    decoded_text = ""
    for pair in pairs:
        row1, col1 = 0, 0
        row2, col2 = 0, 0

        # Find the positions of the characters in the key square
        for i in range(5):
            for j in range(5):
                if key_matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                if key_matrix[i][j] == pair[1]:
                    row2, col2 = i, j

        # Decode the pair of characters
        if row1 == row2:  # Same row
            decoded_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decoded_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:  # Different row and column
            decoded_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return decoded_text
r.sendline(decode_playfair(alphabet, encrypted).lower())
r.interactive()
