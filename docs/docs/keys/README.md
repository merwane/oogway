---
title: Keys overview
---

# Keypairs

According to the [Bitcoin Wiki](https://en.bitcoin.it/wiki/Private_key), a private key is a secret number that allows bitcoins to be spent. The private keys are mathematically related to Bitcoin addresses generated for the wallet. The combination of a private and a public key is a **keypair**.

## Generate a keypair

Generating a keypair using oogway only takes one line of code:

```python
>>> from oogway import Key
>>> key = Key()
```

You can also have your own parameters to generate a keypair accordingly:

```python
>>> from oogway import Key
>>> key = Key(testnet=True, mnemonic_strength=128, passphrase="oogway")
>>>
>>> key.wif
>>> '93GuvkQxXdf2LV7nBhoJQBihWd5wZhYAzVN2uojwmaaey6g2tiu'
>>>
>>> key.address("Bech32")
>>> 'tb1qnrg9smqrsyjzrcwx2fm022kp999fcduvfggtl0rzmxgpz4c6qlzspyac9f'
>>>
>>> key.mnemonic
>>> 'consider cube coral ball improve return lucky dinosaur ticket put gas sense'
```

Or import your own mnemonic and add a passphrase:

```python
>>> from oogway import Key
>>> mnemonic = "reward spider nephew busy face ability thank liar explain close tip barrel"
>>>
>>> key = Key(mnemonic=mnemonic, passphrase="freedom")
>>>
>>> key.wif
>>> '5JKzpxfEi36n7R5ZFnzDLpnxqfbfCYouEdQmZxobrE2ewBKePWv'
>>>
>>> key.address("P2PKH")
>>> '1NFT7SGA56jSGjEtv1CWKAW3cfDS3Bb9EL'
>>>
>>> key.pubkey("c")
>>> '03c26f555207069ff4d669ee74657beb386ba3e18b903fb7f5a1b4b14a71d0eaa6'
```

## CLI

Another thing you can do is generate a keypair using the CLI:

```console
$ oogway keypair --address Bech32 --testnet False

------------------------------------
MNEMONIC: relief chalk mail cargo busy echo paper use genius shoot aspect yard
WIF: 5KkUYpoABWvwGjLo4s6KoMn2fYrJ1DLvN8BoZrNiq8ef2fgEpHE
ADDRESS: bc1q7kr667gqmaqhs2kl97flkcz6zr5g2c8a5c5lhy2xfjjmxxfde8eqfuzd7l
------------------------------------

```