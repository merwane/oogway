import hashlib
from .seed.gen import Mnemonic
from .utils.crypto import doublehash256
from .utils.base58 import b58encode
from .address import Address

def gen_hex(_hash):
    """converts private key to hex format"""
    _hex = _hash.hexdigest()
    return _hex
    
def gen_wif(_hashdigest, testnet=False):
    """converts private key to wif and compressed wif format"""
    if testnet == False:
        prefix = b'\x80'
        suffix = b'\x01'
    else:
        prefix = b'\xEF'
        suffix = b'\x01'

    d = prefix + _hashdigest
    checksum = doublehash256(d).digest()[:4]
    checksum_c = doublehash256(d + suffix).digest()[:4]

    wif = b58encode(d + checksum)
    wif_c = b58encode(d + suffix + checksum_c)

    return wif, wif_c

class Key:
    def __init__(self, mnemonic=None, testnet=False, mnemonic_strength=256, passphrase=""):
        self.hex = ""
        self.wif = ""
        self.wif_c = ""
        self.hash = ""
        self.hashdigest = ""
        self.seed = None
        self.mnemonic = mnemonic
        self.testnet = testnet
        
        mn = Mnemonic()
        if self.mnemonic == None:
            self.mnemonic = mn.generate(strength=mnemonic_strength)
        else:
            pass
        self.seed = mn.to_seed(mnemonic=self.mnemonic, passphrase=passphrase)

        self.hash = hashlib.sha256(self.seed)
        self.hashdigest = self.hash.digest()

        # format private keys
        self.hex = gen_hex(self.hash)
        self.wif, self.wif_c = gen_wif(self.hashdigest, testnet=testnet)
        
    def address(self, _format='Bech32'):
        """returns generated address in selected format | default is bech32"""
        _address = Address(self.hash, testnet=self.testnet)
        _format = _format.lower()
        if _format == 'bech32':
            a = _address.bech32
        elif _format == 'p2pkh':
            a = _address.p2pkh
        elif _format == 'p2sh':
            a = _address.p2sh
        else:
            raise ValueError("Address format %s does not exist" % _format)
        
        return a

    def pubkey(self, _format='unc'):
        """returns generated public key in selected format | default is uncompressed"""
        _pubkey = Address(self.hash, testnet=self.testnet)
        _format = _format.lower()
        if _format == 'unc':
            pb = _pubkey.pubkey
        elif _format == 'c':
            pb = _pubkey.pubkey_c
        else:
            raise ValueError("Public key format %s does not exist" % _format)

        return pb
