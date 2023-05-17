def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    shift_array = list(keyword)
    for i in range(len(shift_array)):
        if shift_array[i] in en_ABC or shift_array[i] in en_abc:
            if shift_array[i].islower():
                shift_array[i] = en_abc.find(shift_array[i])
            elif shift_array[i].isupper():
                shift_array[i] = en_ABC.find(shift_array[i])
        elif shift_array[i] in ru_ABC or shift_array[i] in ru_abc:
            if shift_array[i].islower():
                shift_array[i] = ru_abc.find(shift_array[i])
            elif shift_array[i].isupper():
                shift_array[i] = ru_ABC.find(shift_array[i])
    for i in range(len(plaintext)):
        if plaintext[i] in en_ABC or plaintext[i] in en_abc:
            if plaintext[i].islower():
                ciphertext += en_abc[(en_abc.find(plaintext[i]) + shift_array[i % len(keyword)]) % 26]
            if plaintext[i].isupper():
                ciphertext += en_ABC[(en_ABC.find(plaintext[i]) + shift_array[i % len(keyword) ]) % 26]
        elif plaintext[i] in ru_ABC or plaintext[i] in ru_abc:
            if plaintext[i].islower():
                ciphertext += ru_abc[(ru_abc.find(plaintext[i]) + shift_array[i % len(keyword)]) % 26]
            if plaintext[i].isupper():
                ciphertext += ru_ABC[(ru_ABC.find(plaintext[i]) + shift_array[i] % len(keyword)) % 26]
        else:
            ciphertext += plaintext[i]
    return ciphertext



def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    en_abc = 'abcdefghijklmnopqrstuvwxyz'
    ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    shift_array = list(keyword)
    for i in range(len(shift_array)):
        if shift_array[i] in en_ABC or shift_array[i] in en_abc:
            if shift_array[i].islower():
                shift_array[i] = en_abc.find(shift_array[i])
            elif shift_array[i].isupper():
                shift_array[i] = en_ABC.find(shift_array[i])
        elif shift_array[i] in ru_ABC or shift_array[i] in ru_abc:
            if shift_array[i].islower():
                shift_array[i] = ru_abc.find(shift_array[i])
            elif shift_array[i].isupper():
                shift_array[i] = ru_ABC.find(shift_array[i])
    for i in range(len(ciphertext)):
        if ciphertext[i] in en_ABC or ciphertext[i] in en_abc:
            if ciphertext[i].islower():
                plaintext += en_abc[(en_abc.find(ciphertext[i]) - shift_array[i % len(keyword)]) % 26]
            if ciphertext[i].isupper():
                plaintext += en_ABC[(en_ABC.find(ciphertext[i]) - shift_array[i % len(keyword)]) % 26]
        elif ciphertext[i] in ru_ABC or ciphertext[i] in ru_abc:
            if ciphertext[i].islower():
                plaintext += ru_abc[(ru_abc.find(ciphertext[i]) - shift_array[i % len(keyword)]) % 26]
            if ciphertext[i].isupper():
                plaintext += ru_ABC[(ru_ABC.find(ciphertext[i]) - shift_array[i % len(keyword)]) % 26]
        else:
            plaintext += ciphertext[i]
    return plaintext


