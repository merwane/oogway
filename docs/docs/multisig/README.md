---
title: Multisig overview
---

# Multisig

According to the [Bitcoin Wiki](https://en.bitcoin.it/wiki/Multisignature), Multisignature refers to requiring multiple keys to authorize a Bitcoin transaction, rather than a single signature from one key. Using oogway, it is possible to generate a Multisig key by providing a private key as well as two or more public keys, and the number of signatures required to allow a transaction.

## Generate a multisig key

Generating a 2-of-2 multisig key:

```python
>>> from oogway import Tx, MultiSig
>>> key1 = Tx(wif="93GuvkQxXdf2LV7nBhoJQBihWd5wZhYAzVN2uojwmaaey6g2tiu", network="testnet")
>>> key2 = Tx(wif="931NNGYCcMPZVbB5uDh3MJx23rSf5yzpzH6NgG525mbviVhFF76", network="testnet")
>>>
>>> multisig = MultiSig(key1, {key1.public_key, key2.public_key}, 2, network="testnet")
>>> multisig.address
'2Mu8WMjY3z5fmXcrWmiH9pLLqmUiefC58Mt'
```

## Sign a multisig transaction

Signing and broadcasting a transaction using the 2-of-2 multisig key:

```python
>>> from oogway import Net
>>> multisig2 = MultiSig(key2, {key1.public_key, key2.public_key}, 2, network="testnet")
>>> tx1 = multisig.create_transaction([('myW1WFWyXQ2BKXLM9Uk5jBXuXZmFNWRTFu', 10000)])
>>> tx2 = multisig2.sign_transaction(tx1) # 2nd key
>>> # broadcast
>>> Net(network='testnet').broadcast(tx2)
```