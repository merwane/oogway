from oogway.validate import _bech32check, p2pkh_val, p2sh_val, bech32_val, validate
from tests.data import *

def test__bech32check():
    """validate Bech32 format by encoding only"""
    assert _bech32check(BECH32_ADDRESS) == True
    assert _bech32check(INVALID_BECH32_ADDRESS) == False

def test_p2pkh_val():
    """validate P2PKH format"""
    assert p2pkh_val(P2PKH_ADDRESS) == True
    assert p2sh_val(INVALID_P2PKH_ADDRESS) == False

def test_p2sh_val():
    """validate P2SH format"""
    assert p2sh_val(P2SH_ADDRESS) == True
    assert p2sh_val(INVALID_P2SH_ADDRESS) == False

def test_bech32_val():
    """validate Bech32 format"""
    assert bech32_val(BECH32_ADDRESS) == True
    assert bech32_val(INVALID_BECH32_ADDRESS) == False

def test_address_format():
    """returns address format"""
    bech32 = validate.address_format(BECH32_ADDRESS)
    p2sh = validate.address_format(P2SH_ADDRESS)
    p2pkh = validate.address_format(P2PKH_ADDRESS)

    assert bech32 == 'Bech32'
    assert p2sh == 'P2SH'
    assert p2pkh == 'P2PKH'
