import time
from urllib.parse import quote, urlparse, parse_qs
from .validate import validate
from .convert import convert

def request_payment(address, amount, exp=0, message=""):
    """form a payment request"""
    if validate.is_valid_address(address) == True:
        pass
    else:
        raise ValueError("Invalid Bitcoin address")
    
    btc = convert.to_btc(amount, string=True)

    now = time.time()
    now = int(now)
    now = str(now)
    
    if exp == 0:
        exp_str = ""
    else:
        exp = exp * 60
        exp = str(exp)
        exp_str = ("&exp=%s" % exp)

    if message == "":
        msg = ""
    else:
        if len(message) <= 120:
            message = quote(message)
            msg = ("&message=%s" % message)
        else:
            raise ValueError("Message must be smaller than 120 characters")

    req = ("bitcoin:%s?amount=%s&time=%s%s%s" % (address, btc, now, exp_str, msg))

    return req

def parse_request(uri):
    req = urlparse(uri)
    query = parse_qs(req.query)
    res = {}
    res['address'] = req.path
    res['amount'] = query['amount'][0]
    try:
        res['created'] = query['time'][0]
    except KeyError:
        res['created'] = 0

    res['status'] = "valid"

    try:
        res['exp'] = query['exp'][0]
        now = time.time()
        now = int(now)
        limit = int(res['created']) + int(res['exp'])
        if now > limit:
            res['status'] = "expired"
    except KeyError:
        pass

    try:
        res['message'] = query['message'][0]
    except KeyError:
        pass
    
    res['amount'] = convert.to_satoshi(res['amount'], string=True)
    
    if res['created'] != 0:
        created = int(res['created'])
        res['created'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created))

    return res
