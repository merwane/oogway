---
title: Reference
---

# Operation reference

## BTC operations

**oogway.operation.add_btc(** *values, unit="BTC" **)**

**Parameters:**
* ***values**[int | float | decimal.Decimal]: _Values in BTC._

* **unit**[str]: _Unit returned. Set to `BTC` or `Satoshi`._

**Returns:**
* [decimal.Decimal | int]: _Returns sum in selected unit._

---------

**oogway.operation.substract_btc(** btc_a, btc_b, unit="BTC" **)**

**Parameters:**
* **btc_a**[int | float | decimal.Decimal]: _Value in BTC._

* **btc_b**[int | float | decimal.Decimal]: _Value in BTC._

* **unit**[str]: _Unit returned. Set to `BTC` or `Satoshi`._

**Returns:**
* [decimal.Decimal | int]: _Returns value in selected unit._



## Satoshi operations

**oogway.operation.add_sats(** *values, unit="Satoshi" **)**

**Parameters:**
* ***values**[int]: _Values in Satoshi._

* **unit**[str]: _Unit returned. Set to `BTC` or `Satoshi`._

**Returns:**
* [decimal.Decimal | int]: _Returns sum in selected unit._

---------

**oogway.operation.substract_sats(** sat_a, sat_b, unit="Satoshi" **)**

**Parameters:**
* **sat_a**[int]: _Value in Satoshi._

* **sat_b**[int]: _Value in Satoshi._

* **unit**[str]: _Unit returned. Set to `BTC` or `Satoshi`._

**Returns:**
* [decimal.Decimal | int]: _Returns value in selected unit._

---------