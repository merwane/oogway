---
title: Reference
---

# Conversion reference

## Convert

**oogway.convert.to_satoshi(** amount, string=False **)**

**Parameters:**
* **amount**[float | int | str]: _A value in BTC up to 8 decimals._

* **string**[bool]: _Returns the converted value a string if set to `True`._

**Returns:**
* [int]: _Returns the converted value in Satoshi._

---------

**oogway.convert.to_btc(** amount, string=False **)**

**Parameters:**
* **amount**[int | str]: _A value in Satoshi._

* **string**[bool]: _Returns the converted value a string if set to `True`._

**Returns:**
* [decimal.Decimal]: _Returns the converted value in BTC._