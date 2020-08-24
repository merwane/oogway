from .utils.base58 import b58check
from .utils.bech32 import bech32_decode
import re

ADDRESS_REGEX = "^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
P2PKH_REGEX = "^[1][a-km-zA-HJ-NP-Z1-9]{25,34}$"
P2SH_REGEX = "^[3][a-km-zA-HJ-NP-Z1-9]{25,34}$"
BECH32_REGEX = "^bc1[ac-hj-np-zAC-HJ-NP-Z02-9]{11,71}$"

def _bech32check(address):
    """decodes bech32 address to check validity"""
    a = bech32_decode(address)
    if a == (None, None):
        return False
    else:
        return True

def p2pkh_val(address):
    """check P2PKH address validity"""
    regex = re.match(P2PKH_REGEX, address)
    encoding = b58check(address)
    if regex and encoding:
        return True
    else:
        return False

def p2sh_val(address):
    """check P2SH address validity"""
    regex = re.match(P2SH_REGEX, address)
    encoding = b58check(address)
    if regex and encoding:
        return True
    else:
        return False

def bech32_val(address):
    """check Bech32 address validity"""
    regex = re.match(BECH32_REGEX, address)
    encoding = _bech32check(address)
    if regex and encoding:
        return True
    else:
        return False

class validate:
    """
    validate addresses by format
    or validate regardless of
    format (general)
    """
    @staticmethod
    def is_p2pkh(_address):
        """validate P2PKH addresses"""
        a = p2pkh_val(_address)
        return a
    
    @staticmethod
    def is_p2sh(_address):
        """validate P2SH addresses"""
        a = p2sh_val(_address)
        return a
    
    @staticmethod
    def is_bech32(_address):
        """validate Bech32 addresses"""
        a = bech32_val(_address)
        return a
    
    @staticmethod
    def is_valid_address(_address):
        """validate all addresses format"""
        p2pkh = p2pkh_val(_address)
        p2sh = p2sh_val(_address)
        bech32 = bech32_val(_address)

        if any([p2pkh, p2sh, bech32]):
            a = True
        else:
            a = False

        return a

    @staticmethod
    def address_format(_address):
        bech32 = bech32_val(_address)
        p2sh = p2sh_val(_address)
        p2pkh = p2pkh_val(_address)

        if bech32 == True:
            f = 'Bech32'
        elif p2sh == True:
            f = 'P2SH'
        elif p2pkh == True:
            f = 'P2PKH'
        else:
            raise ValueError("Invalid address")

        return f
