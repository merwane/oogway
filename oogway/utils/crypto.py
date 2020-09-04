import hashlib
from binascii import hexlify
from hashlib import new, sha256 as _sha256
from coincurve import PrivateKey as ECPrivateKey, PublicKey as ECPublicKey

def doublehash256(v):
    return hashlib.sha256(hashlib.sha256(v).digest())

def bytes_to_hex(bytestr, upper=False):
    hexed = hexlify(bytestr).decode()
    return hexed.upper() if upper else hexed



def sha256(bytestr):
    return _sha256(bytestr).digest()


def double_sha256(bytestr):
    return _sha256(_sha256(bytestr).digest()).digest()


def double_sha256_checksum(bytestr):
    return double_sha256(bytestr)[:4]


def ripemd160_sha256(bytestr):
    return new('ripemd160', sha256(bytestr)).digest()


hash160 = ripemd160_sha256