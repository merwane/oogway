---
title: Reference
---

# Transaction reference

## Tx

**oogway.Tx(** wif, network="mainnet" **)**

**Parameters:**
* **wif**[str]: _Private key in WIF format._

* **network**[str]: _Network._ (`mainnet`, `testnet`)

---------

**oogway.Tx.create_transaction(** outputs, fee, leftover, unspents **)**

**Parameters:**
* **outputs**[[tuple]]: _Array of outputs consisting of receiver address + amount in satoshi._
    * e.g: ```[('1FHXDkRLhoCziRjftaPB3fELUYrZomFanx', 100000), ('1Archive1n2C579dMsAu3iC6tWzuQJz8dN', 100000)] ```

* **fee**[int]: Transaction fee in Satoshis per byte._ If no fee is specified, the fastest fee will be calculated and used.
* **leftover**[str]: _Address receiving leftover._ If no address is specified, the leftover will be sent back to the sender address.
* **unspents**[array]: _Unspents of sender address._ If no unspents are specified, they will be queried automatically.

**Returns:**
* [str]: _Raw transaction in hex format._

---------

**oogway.Tx.send(** outputs, fee, leftover, unspents **)**

**Parameters:**
* **outputs**[[tuple]]: _Array of outputs consisting of receiver address + amount in satoshi._
    * e.g: ```[('1FHXDkRLhoCziRjftaPB3fELUYrZomFanx', 100000), ('1Archive1n2C579dMsAu3iC6tWzuQJz8dN', 100000)] ```

* **fee**[int]: Transaction fee in Satoshis per byte._ If no fee is specified, the fastest fee will be calculated and used.
* **leftover**[str]: _Address receiving leftover._ If no address is specified, the leftover will be sent back to the sender address.
* **unspents**[array]: _Unspents of sender address._ If no unspents are specified, they will be queried automatically.

**Returns:**
* [str]: _Hash of the broadcasted transaction._