import decimal
from .convert import convert

class operation:

    @staticmethod
    def add_sats(*sats, unit="satoshi"):
        """addition operation on sats"""
        res = 0
        for sat in sats:
            if type(sat) != int:
                raise ValueError("Satoshi values must be integers")
            if sat <= 0:
                raise ValueError("Satoshi values must be positive")
            res += sat
        
        unit = unit.lower()
        if unit == 'satoshi':
            pass
        elif unit == 'btc':
            res = convert.to_btc(res, string=False)
        else:
            raise ValueError("Unit %s does not exist" % unit)

        return res

    @staticmethod
    def substract_sats(sat_a, sat_b, unit="satoshi"):
        """substraction operation on sats"""
        if type(sat_a) != int or type(sat_b) != int:
            raise ValueError("Satoshi values must be integers")
        
        if sat_a <= 0 or sat_b <= 0:
            raise ValueError("Satoshi values must be positive")
        
        if sat_b > sat_a:
            raise ValueError("Result cannot be negative")

        res = sat_a - sat_b

        unit = unit.lower()
        if unit == 'satoshi':
            pass
        elif unit == 'btc':
            res = convert.to_btc(res, string=False)
        else:
            raise ValueError("Unit %s does not exist" % unit)

        return res

    @staticmethod
    def add_btc(*btcs, unit="btc"):
        """addition operation on btc"""
        res = 0
        for btc in btcs:
            if type(btc) == int:
                pass
            elif type(btc) == float:
                pass
            elif type(btc) == decimal.Decimal:
                pass
            else:
                raise ValueError("BTC values must be numbers")
            if btc <= 0:
                raise ValueError("BTC values must be positive")
            res += btc
        
        unit = unit.lower()
        res = round(res, 8)
        res = decimal.Decimal(res)
        res = round(res, 8)
        if unit == 'btc':
            pass
        elif unit == 'satoshi':
            res = convert.to_satoshi(res, string=False)
        else:
            raise ValueError("Unit %s does not exist" % unit)

        return res

    @staticmethod
    def substract_btc(btc_a, btc_b, unit="btc"):
        """substraction operation on BTC"""
        if type(btc_a) == int:
            pass
        elif type(btc_a) == float:
            pass
        elif type(btc_a) == decimal.Decimal:
            pass
        else:
            raise ValueError("BTC values must be numbers")

        if type(btc_b) == int:
            pass
        elif type(btc_b) == float:
            pass
        elif type(btc_b) == decimal.Decimal:
            pass
        else:
            raise ValueError("BTC values must be numbers")
        
        if btc_a <= 0 or btc_b <= 0:
            raise ValueError("BTC values must be positive")
        
        if btc_b > btc_a:
            raise ValueError("Result cannot be negative")

        res = btc_a - btc_b

        unit = unit.lower()
        res = round(res, 8)
        res = decimal.Decimal(res)
        res = round(res, 8)
        if unit == 'btc':
            pass
        elif unit == 'satoshi':
            res = convert.to_satoshi(res, string=False)
        else:
            raise ValueError("Unit %s does not exist" % unit)

        return res
