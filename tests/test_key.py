import pytest
from oogway.key import Key
from tests.data import *
from oogway.validate import validate
import _hashlib

keys = []
def gen_keys(mnemonic=None, _range=10, _append=True):
    i_keys = []
    for _ in range(_range):
        key = Key(mnemonic)
        if _append == True:
            keys.append(key)
        else:
            i_keys.append(key)
    return i_keys

gen_keys()

@pytest.mark.parametrize("key", keys)
def test_key_generation(key):
    """check key formats type"""
    assert type(key.hash) is _hashlib.HASH
    assert type(key.wif) is str
    assert type(key.hex) is str
    assert type(key.seed) is bytes
    assert type(key.hashdigest) is bytes
    assert type(key.mnemonic) is str

@pytest.mark.parametrize("key", keys)
def test_address_generation(key):
    """validate addresses format"""
    bech32 = key.address('bech32')
    p2pkh = key.address('p2pkh')
    p2sh = key.address('p2sh')
    default_address = key.address()
    
    assert validate.is_bech32(bech32) == True
    assert validate.is_p2pkh(p2pkh) == True
    assert validate.is_p2sh(p2sh) == True
    assert validate.is_bech32(default_address) == True

def test_generation_regularity():
    """check if mnemonic product is regular"""
    _keys = gen_keys(MNEMONIC_1, 3, False)
    wifs = []
    bech32_addresses = []
    p2pkh_addresses = []
    for key in _keys:
        wifs.append(key.wif)
        bech32_addresses.append(key.address('bech32'))
        p2pkh_addresses.append(key.address('p2pkh'))

    wif_result = wifs.count(wifs[0]) == len(wifs)
    bech32_address_result = bech32_addresses.count(bech32_addresses[0]) == len(bech32_addresses)
    p2pkh_address_result = p2pkh_addresses.count(p2pkh_addresses[0]) == len(p2pkh_addresses)

    assert wif_result == True
    assert bech32_address_result == True
    assert p2pkh_address_result == True

@pytest.mark.parametrize("key", keys)
def test_pubkey_format(key):
    pubkey = key.pubkey('unc')
    pubkey_len = len(pubkey)
    
    pubkey_c = key.pubkey('c')
    pubkey_c_len = len(pubkey_c)

    assert pubkey_len == 130
    assert pubkey_c_len == 66
    assert pubkey[0] == '0'
    assert pubkey_c[0] == '0'