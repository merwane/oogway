import binascii
import hashlib
import ecdsa
from .utils.base58 import b58encode
from .utils import bech32
from .utils.crypto import doublehash256

def hash160(v):
    r = hashlib.new('ripemd160')
    r.update(hashlib.sha256(v).digest())
    return r

def SECP256k1(digest):
    sk = ecdsa.SigningKey.from_string(digest, curve=ecdsa.SECP256k1)
    return sk.get_verifying_key()

def gen_p2pkh(_hash, testnet=False):
    """generate p2pkh address (prefix is 1)"""
    if testnet == False:
        prefix_a = b'\x04'
        prefix_b = b'\x00'
    else:
        prefix_a = b'\x04'
        prefix_b = b'\x6F'
    address = gen_unc_pub(_hash, prefix_a, prefix_b)
    return address

def gen_p2sh(_hash, testnet=False):
    """generate p2sh address (prefix is 3)"""
    if testnet == False:
        prefix = b'\x05'
    else:
        prefix = b'\xC4'
    address = _gen_p2sh(_hash, prefix)
    return address

def _gen_p2sh(_hash, prefix):
    """generate p2sh address (prefix is 3)"""
    prefix_redeem = b'\x00\x14'
    p = gen_c_pub(_hash, b'\x02', b'\x03')
    redeem_script = hash160(prefix_redeem + hash160(p).digest()).digest()
    m = prefix + redeem_script
    checksum = doublehash256(m).digest()[:4]
    address = b58encode(m + checksum)
    return address

def gen_bech32(_hash, testnet=False):
    """generate bech32 P2WSH address (prefix is bc1 | tb1)"""
    if testnet == False:
        prefix_a = b'\x02'
        prefix_b = b'\x03'
        address_prefix = 'bc'
    else:
        prefix_a = b'\x02'
        prefix_b = b'\x14'
        address_prefix = 'tb'
    p = gen_c_pub(_hash, prefix_a, prefix_b)
    redeem_script_P2WSH = hashlib.sha256(p).digest()
    address = str(bech32.encode(address_prefix, 0x00, redeem_script_P2WSH))
    return address

def gen_unc_pub(_hash, prefix_a, prefix_b):
    """generate uncompressed pubkey from hash"""
    digest = _hash.digest()
    p = prefix_a + SECP256k1(digest).to_string()
    pubkey = str(binascii.hexlify(p).decode('utf-8'))
    _hash160 = hash160(p)
    m = prefix_b + _hash160.digest()
    checksum = doublehash256(m).digest()[:4]

    unc = b58encode(m + checksum)
    return unc

def _gen_unc_pub(_hash):
    digest = _hash.digest()
    p = b'\x04' + SECP256k1(digest).to_string()
    pubkey = str(binascii.hexlify(p).decode('utf-8'))
    return pubkey

def gen_c_pub(_hash, prefix_even, prefix_odd):
    """generate compressed pubkey from hash"""
    prefix_a = prefix_odd
    digest = _hash.digest()
    ecdsa_digest = SECP256k1(digest).to_string()
    x_coord = ecdsa_digest[:int(len(ecdsa_digest) / 2)]
    y_coord = ecdsa_digest[int(len(ecdsa_digest) / 2):]
    if (int(binascii.hexlify(y_coord), 16) % 2 == 0): prefix_a = prefix_even
    p = prefix_a + x_coord
    c = str(binascii.hexlify(p).decode('utf-8'))
    return p

def _gen_c_pub(_hash):
    prefix_a = b'\x03'
    prefix_even = b'\x02' 
    digest = _hash.digest()
    ecdsa_digest = SECP256k1(digest).to_string()
    x_coord = ecdsa_digest[:int(len(ecdsa_digest) / 2)]
    y_coord = ecdsa_digest[int(len(ecdsa_digest) / 2):]
    if (int(binascii.hexlify(y_coord), 16) % 2 == 0): prefix_a = prefix_even
    p = prefix_a + x_coord
    c = str(binascii.hexlify(p).decode('utf-8'))
    return c

class Address:
    def __init__(self, _hash, testnet=False):
        self.pubkey = _gen_unc_pub(_hash)
        self.pubkey_c = _gen_c_pub(_hash)
        self.p2pkh = gen_p2pkh(_hash, testnet)
        self.p2sh = gen_p2sh(_hash, testnet)
        self.bech32 = gen_bech32(_hash, testnet)
