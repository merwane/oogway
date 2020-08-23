---
title: Reference
---

# Keys reference

## Key

**oogway.Key(** mnemonic=None, testnet=False, mnemonic_strength=256, passphrase="" **)**

**Parameters:**
* **mnemonic**[str]: _A list of words which store all the information needed to generate or recover a Bitcoin wallet._ Use this for importing your own mnemonic phrase.

* **testnet**[bool]: _An alternative Bitcoin blockchain, to be used for testing._ Set this to `True` for generating testnet keypairs.

* **mnemonic_strength**[int]: _Strength for performing a mnemonic phrase generation. Expressed in bits._ Set this to `128` for generating a 12 words phrase, or `256` for a 24 words phrase (recommended). This parameter will be ignored if you import your own mnemonic phrase.

* **passphrase**[str]: _A passphrase to be used with your mnemonic phrase to generate a unique seed._ A passphrase is usually used like a password.

**Returns:**
* **hex**[str]: _Private key in hex format._
* **wif**[str]: _Private key in WIF format._
* **wif_c**[str]: _Private key in compressed WIF format._
* **seed**[bytes]: _Generated seed._
* **mnemonic**[str]: _Generated mnemonic phrase._
* **testnet**[bool]: _Returns `True` if the generated keypair is for testnet._

## Address

**oogway.Key().address(** _format="Bech32" **)**

**Parameters:**
* **_format**[str]: _Format of the generated address._ Can be set to `P2PKH` for an address with a prefix of _1_, `P2SH` for a prefix of _3_, or `Bech32` for a segwit address with a prefix of _bc1_ (recommended).

::: warning Note
If `Key` is set to testnet, the prefixes will be different. For example, Bech32 addresses will be returned with a prefix of _tb1_.
:::

**Returns:**
* [str]: _Mainnet or testnet address._

## Pubkey

**oogway.Key().pubkey(** _format="unc" **)**

**Parameters:**
* **_format**[str]: _Format of the generated public key._ Can be set to `c` for a compressed public key, or `unc` for an uncompressed public key.

**Returns:**
* [str]: _Public key._