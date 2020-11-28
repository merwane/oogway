---
title: Reference
---

# Network reference

## Net

**oogway.Net(** provider="Blockstream", network="mainnet" **)**

**Parameters:**
* ***provider**[str]: _API Provider._ (`Blockstream` | `Blockchair`)

* **network**[str]: _Bitcoin network._ (`mainnet` | `testnet`)

---------

## Balance

**oogway.Net.balance(** address, unit="satoshi" **)**

**Parameters:**
* **address:**[str]: _Valid Bitcoin address._

* **unit:**[str]: _Bitcoin unit._ (`satoshi`, `btc`)

**Returns:**
* [int | decimal.Decimal]: _Address final balance._

---------

## Transactions

**oogway.Net.txs(** address **)**

**Parameters:**
* **address:**[str]: _Valid Bitcoin address._

**Returns:**
* [[str]]: _Transaction hashes._

---------

## Unspents

**oogway.Net.utxo(** address **)**

**Parameters:**
* **address:**[str]: _Valid Bitcoin address._

**Returns:**
* [[dict]]: 
    * **value**[int]: _Unspent value._
    * **confirmations**[int]: _Number of confirmations._
    * **script**[str]: _Script._
    * **hash**[str]: _Transaction hash._
    * **index**[int]: _Index._

---------

## Broadcast

**oogway.Net.txs(** tx_hex **)**

**Parameters:**
* **tx_hex**[str]: _Raw transaction in hex format._

**Returns:**
* [bool]: _Broadcast status._ (`True`, `False`)

--------

## Transaction explorer

**oogway.Net.transaction(** txid **)**

**Parameters:**
* **tx_hex**[str]: _Transaction ID._

**Returns:**
* [dic]: _Transaction information._
