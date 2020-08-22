import decimal

ONE_BTC_SAT = int(1e8)

class convert:

    @staticmethod
    def to_satoshi(amount, string=False):
        """convert from btc to satoshi"""
        if type(amount) == str:
            amount = float(amount)
        if amount < 0:
            raise ArithmeticError("BTC amount must be a positive number")

        safe = round(amount, 8)
        safe = "{:.8f}".format(amount)
        safe = float(safe) * ONE_BTC_SAT
        safe = int(safe)
        
        if string == False:
            pass
        else:
            safe = str(safe)

        return safe

    @staticmethod
    def to_btc(amount, string=False):
        """convert from satoshi to btc"""
        if type(amount) == str:
            amount = int(amount)
        d = decimal.Decimal(str(amount))
        precision = d.as_tuple().exponent
        
        if precision != 0:
            raise ArithmeticError("Satoshi amount must be an integer")
        if amount < 0:
            raise ArithmeticError("Satoshi amount must be a positive number")

        safe = amount / ONE_BTC_SAT
        safe = round(safe, 8)
        if string == False:
            safe = decimal.Decimal(safe)
            safe = round(safe, 8)
        else:
            safe = "{:.8f}".format(safe)
        
        return safe
