from oogway.fees import get_fees

def test_get_fees():
    fastest = get_fees('fastest')
    three = get_fees('3')
    six = get_fees('6')

    assert type(fastest) == int
    assert type(three) == int
    assert type(six) == int
