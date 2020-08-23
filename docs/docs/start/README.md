---
title: Introduction
---

## What can oogway do?

**oogway** is a secure Bitcoin utility library for Python.

The library allows you to easily generate Bitcoin keypairs with very good security and entropy. It can also do other things such as validate addresses (cryptographically) or safely convert and operate between bitcoin units.

Here's an example for generating a keypair and a 24 words mnemonic phrase:

```python
>>> from oogway import Key
>>>
>>> key = Key(mnemonic_strength=256, passphrase="bitcoin")
>>>
>>> key.mnemonic
'hungry believe click napkin aerobic make skirt early vibrant suffer trumpet pupil prize ecology bleak citizen absent chief feed skin vast enter this female'
>>>
>>> key.wif # wif private key
'5JnkYopgMsFQtsUkZ3WkmacsBGk3JouYpUNpudHDp6VW3QyyJEr'
>>>
>>> key.address("Bech32") # Bech32 (segwit) address
'bc1qt8felv4tn8a4kzjqle4r5scerwda9pmmaza95xyp22wtnccxhz7snrumvq'
>>>
>>> key.pubkey("unc") # uncompressed public key
'041d5e3b36948035f6cee1d349e02fa3c8cb2f07c1aa3692abfe2699e7693423162a184b8bf58aec320368ddb58ff16705f3ecfed23f8cc080b1225a0e90a74c6c'
```

## What does oogway mean?

oogway is a [tortoise](https://kungfupanda.fandom.com/wiki/Oogway) that also happens to be the creator of Kung Fu. Even though he seems slow and old to others, he is the unbeaten Grand Master of the art he created.

## License

oogway is licensed under [MIT](https://en.wikipedia.org/wiki/MIT_License).