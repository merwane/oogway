from collections import deque
from hashlib import sha256

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE58_ALPHABET_LIST = list(BASE58_ALPHABET)

def b58encode(bytestr):
    """encode to base58"""
    alphabet = BASE58_ALPHABET_LIST
    encoded = deque()
    append = encoded.appendleft
    _divmod = divmod

    num = int.from_bytes(bytestr, 'big')

    while num > 0:
        num, rem = _divmod(num, 58)
        append(alphabet[rem])
    
    encoded = ''.join(encoded)
    pad = 0
    for byte in bytestr:
        if byte == 0:
            pad += 1
        else:
            break
    
    return '1' * pad + encoded

def b58decode(bytestr, length):
    """decode from base58"""
    n = 0
    for char in bytestr:
        n = n * 58 + BASE58_ALPHABET.index(char)
    return n.to_bytes(length, 'big')

def b58check(bytestr):
    """check if base58 encoded address is valid"""
    try:
        bcbytes = b58decode(bytestr, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False
