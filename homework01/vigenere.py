def encrypt_vigenere(plaintext, keyword):
    """
        >>> encrypt_vigenere("PYTHON", "A")
        'PYTHON'
        >>> encrypt_vigenere("python", "a")
        'python'
        >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
        'LXFOPVEFRNHR'
        """
    encrypted = list()
    for i in range(0, len(plaintext)):
        if plaintext[i].lower() < 'a' or plaintext[i].lower() > 'z':
            encrypted.append(plaintext[i])
            continue
        key = ord(keyword[i % len(keyword)].upper())
        encrypted.append(chr(ord('A') + (ord(plaintext[i].upper()) + key) % 26))
        if plaintext[i].islower():
            encrypted[i] = encrypted[i].lower()
    return ''.join(encrypted)


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    decrypted = list()
    for i in range(0, len(ciphertext)):
        if ciphertext[i].lower() < 'a' or ciphertext[i].lower() > 'z':
            decrypted.append(ciphertext[i])
            continue
        key = ord(keyword[i % len(keyword)].upper())
        decrypted.append(chr(ord('A') + (ord(ciphertext[i].upper()) - key) % 26))
        if ciphertext[i].islower():
            decrypted[i] = decrypted[i].lower()
    return ''.join(decrypted)

