import os
import hashlib
import binascii
import hmac
from .base58 import b58encode

class Mnemonic:
    def __init__(self):
        with open("%s/english.txt" % (self._get_directory()), "r", encoding="utf-8") as f:
            self.wordlist = [w.strip() for w in f.readlines()]
    
    @classmethod
    def _get_directory(cls):
        return os.path.join(os.path.dirname(__file__), "wordlist")

    def generate(self, strength=128):
        if strength not in [128, 160, 192, 224, 256]:
            raise ValueError("Strength should be one of the following [128, 160, 192, 224, 256]")
        return self.to_mnemonic(os.urandom(strength // 8))

    def to_mnemonic(self, data):
        h = hashlib.sha256(data).hexdigest()
        b = (
        bin(int(binascii.hexlify(data), 16))[2:].zfill(len(data) * 8)
        + bin(int(h, 16))[2:].zfill(256)[: len(data) * 8 // 32]
        )
        result = []
        for i in range(len(b) // 11):
            idx = int(b[i * 11 : (i + 1) * 11], 2)
            result.append(self.wordlist[idx])
        result_phrase = " ".join(result)
        return result_phrase
    
    @classmethod
    def to_seed(cls, mnemonic, passphrase=""):
        passphrase = "mnemonic"+passphrase
        mnemonic = mnemonic.encode("utf-8")
        passphrase = passphrase.encode("utf-8")
        stretched = hashlib.pbkdf2_hmac("sha512", mnemonic, passphrase, 2048)
        return stretched[:64]

    @classmethod
    def to_hd_master_key(cls, seed):
        if len(seed) != 64:
            raise ValueError("Provided seed should have length of 64")
        seed = hmac.new(b"Bitcoin seed", seed, digestmod=hashlib.sha512).digest()
        xprv = b"\x04\x88\xad\xe4"
        xprv += b"\x00" * 9
        xprv += seed[32:]
        xprv += b"\x00" + seed[:32]

        hashed_xprv = hashlib.sha256(xprv).digest()
        hashed_xprv = hashlib.sha256(hashed_xprv).digest()

        xprv += hashed_xprv[:4]

        return b58encode(xprv)
