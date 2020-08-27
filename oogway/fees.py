import requests
from json.decoder import JSONDecodeError

fees_endpoint_blockstream = "https://blockstream.info/api/fee-estimates"
fees_endpoint_earn = "https://bitcoinfees.earn.com/api/v1/fees/recommended"
HARDCODED_FAST = 100
HARDCODED_THREE_BLOCKS = 95
HARDCODED_SIX_BLOCKS = 55

def get_fees(timeframe="fastest", provider="blockstream"):
    """get fees in satoshis per byte"""
    timeframe = timeframe.lower()
    if timeframe == "fastest":
        tf_bs = "1"
        tf_earn = "fastestFee"
        default_fee = HARDCODED_FAST
    elif timeframe == "3":
        tf_bs = "3"
        tf_earn = "halfHourFee"
        default_fee = HARDCODED_THREE_BLOCKS
    elif timeframe == "6":
        tf_bs = "6"
        tf_earn = "hourFee"
        default_fee = HARDCODED_SIX_BLOCKS
    else:
        raise ValueError("The specified timeframe %s does not exist" % timeframe)
    
    provider = provider.lower()
    if provider == "blockstream":
        endpoint = fees_endpoint_blockstream
    elif provider == "earn":
        endpoint = fees_endpoint_earn
    else:
        raise ValueError("The specified provider %s does not exist" % provider)

    fee = requests.get(endpoint)
    fee = fee.json()
    try:
        if provider == "blockstream":
            fee = int(fee[tf_bs])
        elif provider == "earn":
            fee = fee[tf_earn]
            
    except (KeyError, JSONDecodeError):
        fee = default_fee
    return fee
