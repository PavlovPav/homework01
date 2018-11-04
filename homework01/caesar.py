def encrypt_caesar(plaintext):
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
    res = ''
    for c in plaintext:
        if ord('A') <= ord(c) <= ord ('Z'):
            k = ord(c) + 3
            k = chr((k - ord('A')) % (ord('Z') - ord('A') + 1) + ord('A'))
            res += k
        elif ord('a') <= ord(c) <= ord('z'):
            k = ord(c) + 3
            k = chr((k - ord('a')) % (ord('z') - ord('a') + 1) + ord('a'))
            res += k
        else:
            res += c
    return res


def decrypt_caesar(ciphertext):
    res = ''
    for c in ciphertext:
        if ord('A') <= ord(c) <= ord('Z'):
            k = ord(c) -3
            k = chr((k - ord('A')) % (ord('Z') - ord('A') + 1) + ord('A'))
            res += k
        elif ord('a') <= ord(c) <= ord('z'):
            k = ord(c) - 3
            k = chr((k - ord('a')) % (ord('z') - ord('a') + 1) + ord('a'))
            res += k
        else:
            res += c
    return res
