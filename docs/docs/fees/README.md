---
title: Fees overview
---

# Fees

oogway provides a method to get recommended transaction fees in Satoshis per byte via [Blockstream](https://blockstream.info/) or [Earn.com](https://bitcoinfees.earn.com/).

## Get fees

Generating a keypair using oogway only takes one line of code:

```python
>>> from oogway import get_fees
>>> get_fees('fastest')
98
```

## CLI

You can also get the recommended fees using the CLI:

```console
$ oogway fees --timeframe fastest

> 98 Satoshis/byte
```