# oogway
**oogway** is a simple, yet secure Bitcoin utility library for Python.

[![Supported Versions](https://img.shields.io/pypi/pyversions/oogway.svg?&style=flat)](https://pypi.org/project/oogway)
[![Build](https://img.shields.io/travis/merwane/oogway.svg?branch=master&style=flat)](https://pypi.org/project/oogway)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat&logo=bitcoin&color=orange)](https://pypi.org/project/oogway)

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

The library allows you to easily generate Bitcoin keypairs or create, sign and broadcast transactions. It can also do other things such as validate addresses (cryptographically) or safely convert and operate between bitcoin units.

oogway also has a built-in CLI to simplify some tasks:
```console
$ oogway validate 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy 1BWJVUqZKbs6nXbsrh0boyjckqdoKIk5wa

[VALID | P2SH] 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
[INVALID] 1BWJVUqZKbs6nXbsrh0boyjckqdoKIk5wa
```

## Installation
---------------
```console
$ pip install oogway
```

## Documentation
---------------
Read the library documentation at [6conf.com](https://oogway.6conf.com).

The documentation is automatically updated after each commit to the master branch. Every pull request adding or modifying features must contain a documentation update (Markdown).

Docs are generated using [VuePress](https://vuepress.vuejs.org/). To run the docs locally, do:

```console
$ cd docs/
$ npm install
$ npm run docs:dev
```

## Contribute
-------------

Add yourself to [authors](AUTHORS.md) and make a pull request on a new branch. Update the documentation if necessary.


## Notes
-------------
* oogway is one of many Python Bitcoin libraries. It was heavily inspired by [ofek/bit](https://github.com/ofek/bit). oogway tries to focus on security while remaining simple and accessible.