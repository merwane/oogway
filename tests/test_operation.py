from oogway.operation import operation
import decimal

def test_add_sats():
    op_1 = operation.add_sats(1, 1, 1, unit="satoshi")
    op_2 = operation.add_sats(50000000, 50000000, unit="btc")

    assert op_1 == 3
    assert op_2 == decimal.Decimal('1.00000000')
    assert type(op_1) == int
    assert type(op_2) == decimal.Decimal

def test_substract_sats():
    op_1 = operation.substract_sats(10, 1, unit="satoshi")
    op_2 = operation.substract_sats(200000000, 100000000, unit="btc")

    assert op_1 == 9
    assert op_2 == decimal.Decimal('1.00000000')
    assert type(op_1) == int
    assert type(op_2) == decimal.Decimal

def test_add_btc():
    op_1 = operation.add_btc(1, 1, unit="btc")
    op_2 = operation.add_btc(1, 1, unit="satoshi")

    assert op_1 == decimal.Decimal('2.00000000')
    assert op_2 == 200000000
    assert type(op_1) == decimal.Decimal
    assert type(op_2) == int

def test_substract_btc():
    op_1 = operation.substract_btc(2, 1, unit="btc")
    op_2 = operation.substract_btc(2, 1, unit="satoshi")

    assert op_1 == decimal.Decimal('1.00000000')
    assert op_2 == 100000000
    assert type(op_1) == decimal.Decimal
    assert type(op_2) == int
