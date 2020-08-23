---
title: Operation overview
---

# Operation

The operation method can be used for performing safe operations with Satoshi and BTC. In this context, safe means that the operation results will not overflow the maximum decimals for BTC, return a float for Satoshi or return a negative value.

## Addition Satoshi and return BTC

Doing a Satoshi addition and returning the result in BTC is possible in one line of code:

```python
>>> from oogway import operation
>>> operation.add_sats(2000, 3672, 98631, 6, unit="BTC")
Decimal('0.00104309')
```

## Substract BTC and return Satoshi

Reversely, it is possible to do operations such as substracting BTC and returning Satoshi:

```python
>>> from oogway import operation
>>> operation.substract_btc(0.683, 0.0014, unit="Satoshi")
68160000
```