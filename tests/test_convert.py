from oogway.convert import convert
import decimal

def test_to_satoshi():
    one_btc = convert.to_satoshi(amount=1, string=False)
    one_btc_str = convert.to_satoshi(amount=1, string=True)

    assert one_btc == int(1e8)
    assert type(one_btc) == int
    assert one_btc_str == str(int(1e8))
    assert type(one_btc_str) == str

def test_to_btc():
    one_btc_sats = convert.to_btc(amount=int(1e8), string=False)
    one_btc_sats_str = convert.to_btc(amount=int(1e8), string=True)

    assert one_btc_sats == decimal.Decimal('1.00000000')
    assert type(one_btc_sats) == decimal.Decimal
    assert one_btc_sats_str == '1.00000000'
    assert type(one_btc_sats_str) == str
