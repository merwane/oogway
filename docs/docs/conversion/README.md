---
title: Conversion overview
---

# Conversion

The conversion method can be used for doing safe conversions between bitcoin units (BTC, Satoshi). In this context, safe means that the conversions will not overflow the maximum decimals for BTC, return a float for Satoshi or return a negative value.

## Convert from BTC to Satoshi

Doing a BTC to Satoshi conversion using oogway only takes one line of code:

```python
>>> from oogway import convert
>>> convert.to_satoshi(0.00573)
573000
```

## Convert from Satoshi to BTC

Doing a Satoshi to BTC conversion also takes a single line of code:

```python
>>> from oogway import convert
>>> convert.to_btc(192)
Decimal('0.00000192')
```

You can also specify `string=True` as a parameter to return a string instead of a Decimal object:

```python
>>> from oogway import convert
>>> convert.to_btc(42, string=True)
'0.00000042'
```

## CLI

Another thing you can do is convert using the CLI:

```console
$ oogway convert_to_satoshi 1.872

> 1.872 BTC is 187200000 Satoshi

$ oogway convert_to_btc 275000

> 275000 Satoshi is 0.00275000 BTC
```