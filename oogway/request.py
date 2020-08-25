import time
from urllib.parse import quote
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
