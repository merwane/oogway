---
title: Reference
---

# Multisig reference

## Multisig

**oogway.Multisig(** private_key, public_keys, m, network="mainnet" **)**

**Parameters:**
* **private_key**[Tx]: _A Tx object representing a private key._

* **public_keys**[{bytes}]: _A dictionnary containing the public keys of signers._

* **m**[int]: _The number of signatures required to authorize the multisig._

* **network**[str]: _Bitcoin network._ (`mainnet` | `testnet`)

**Returns:**
* **Multisig**[Multisig]: _The Multisig object._

---------

**oogway.Multisig.create_transaction(** outputs, fee, leftover, unspents, lock_time **)**

**Parameters:**
* **outputs**[[tuple]]: _Array of outputs consisting of receiver address + amount in satoshi._
    * e.g: ```[('1FHXDkRLhoCziRjftaPB3fELUYrZomFanx', 100000), ('1Archive1n2C579dMsAu3iC6tWzuQJz8dN', 100000)] ```

* **fee**[int]: Transaction fee in Satoshis per byte._ If no fee is specified, the fastest fee will be calculated and used.
* **leftover**[str]: _Address receiving leftover._ If no address is specified, the leftover will be sent back to the sender address.
* **unspents**[array]: _Unspents of multisig address._ If no unspents are specified, they will be queried automatically.
* **lock_time**[int]: _Epoch time for the transaction to be valid to broadcast, specified in Unix epoch time._ If no locktime is specified, none will be used.

**Returns:**
* [str]: _Raw transaction in hex format._

---------

**oogway.Multisig.sign_transaction(** tx_data, unspents, lock_time **)**

**Parameters:**
* **tx_data**[str]: _Raw transaction in hex format._
* **unspents**[array]: _Unspents of multisig address._ If no unspents are specified, they will be queried automatically.
* **lock_time**[int]: _Epoch time for the transaction to be valid to broadcast, specified in Unix epoch time._ If no locktime is specified, none will be used.

**Returns:**
* [str]: _Raw transaction in hex format._

---------

**oogway.Multisig.get_balance()**

**Returns:**
* [int]: _Address balance in Satoshis._

---------

**oogway.Multisig.get_transactions()**

**Returns:**
* [[str]]: _Transactions._