import requests

fees_endpoint = "https://bitcoinfees.earn.com/api/v1/fees/recommended"
HARDCODED_FAST = 100
HARDCODED_THREE_BLOCKS = 95
HARDCODED_SIX_BLOCKS = 55

def get_fees(timeframe="fastest"):
    """get fees in satoshis per byte"""
    timeframe = timeframe.lower()
    if timeframe == "fastest":
        tf = "fastestFee"
        default_fee = HARDCODED_FAST
    elif timeframe == "3":
        tf = "halfHourFee"
        default_fee = HARDCODED_THREE_BLOCKS
    elif timeframe == "6":
        tf = "hourFee"
        default_fee = HARDCODED_SIX_BLOCKS
    else:
        raise ValueError("The specified timeframe %s does not exist" % timeframe)

    fee = requests.get(fees_endpoint)
    fee = fee.json()
    try:
        fee = fee[tf]
    except KeyError:
        fee = default_fee
    return fee
