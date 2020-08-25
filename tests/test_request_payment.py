from oogway.request import request_payment, parse_request
from oogway.validate import validate

REQ1_RES = "bitcoin:1FHXDkRLhoCziRjftaPB3fELUYrZomFanx?amount=0.00020000&time=1598319207&exp=3600&message=oogway%20requests"

REQ2_RES = "bitcoin:1FHXDkRLhoCziRjftaPB3fELUYrZomFanx?amount=0.00020000&time=1598319712"

def test_request_payment():
    req1 = request_payment("1FHXDkRLhoCziRjftaPB3fELUYrZomFanx", 20000, 60, "oogway requests")
    req2 = request_payment("1FHXDkRLhoCziRjftaPB3fELUYrZomFanx", 20000)

    assert req1[0:66] == REQ1_RES[0:66]
    assert req1[76:] == REQ1_RES[76:]
    assert req2[0:66] == REQ2_RES[0:66]

def test_parse_request():
    req = parse_request(REQ1_RES)
    address = req['address']
    amount = req['amount']
    created = req['created']
    status = req['status']

    assert validate.is_valid_address(address) == True
    assert type(amount) == str
    assert type(created) == str
    assert type(status) == str
