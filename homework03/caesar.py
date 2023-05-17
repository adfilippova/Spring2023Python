import typing as tp
import re


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in range(len(plaintext)):
        if plaintext[i] in en_ABC or plaintext[i] in en_abc:
            if plaintext[i].islower():
                ciphertext += en_abc[(en_abc.find(plaintext[i]) + shift) % 26]
            if plaintext[i].isupper():
                ciphertext += en_ABC[(en_ABC.find(plaintext[i]) + shift) % 26]
        elif plaintext[i] in ru_ABC or plaintext[i] in ru_abc:
            if plaintext[i].islower():
                ciphertext += ru_abc[(ru_abc.find(plaintext[i]) + shift) % 26]
            if plaintext[i].isupper():
                ciphertext += ru_ABC[(ru_ABC.find(plaintext[i]) + shift) % 26]
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in range(len(ciphertext)):
        if ciphertext[i] in en_ABC or ciphertext[i] in en_abc:
            if ciphertext[i].islower():
                plaintext += en_abc[(en_abc.find(ciphertext[i]) - shift) % 26]
            if ciphertext[i].isupper():
                plaintext += en_ABC[(en_ABC.find(ciphertext[i]) - shift) % 26]
        elif ciphertext[i] in ru_ABC or ciphertext[i] in ru_abc:
            if ciphertext[i].islower():
                plaintext += ru_abc[(ru_abc.find(ciphertext[i]) - shift) % 26]
            if ciphertext[i].isupper():
                plaintext += ru_ABC[(ru_ABC.find(ciphertext[i]) - shift) % 26]
        else:
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    text_shift = ciphertext
    while text_shift not in dictionary:
        best_shift += 1
        text_shift = encrypt_caesar(ciphertext, best_shift)
    return best_shift
