import hashlib
from binascii import hexlify

def doublehash256(v):
    return hashlib.sha256(hashlib.sha256(v).digest())

def bytes_to_hex(bytestr, upper=False):
    hexed = hexlify(bytestr).decode()
    return hexed.upper() if upper else hexed