---
title: Reference
---

# Validation reference

## Validate

**oogway.validate.is_p2pkh(** _address **)**

**Parameters:**
* **_address_**[str]: _A valid Bitcoin address._

**Returns:**
* [bool]: _Returns `True` if address is in P2PKH format._

---------

**oogway.validate.is_p2sh(** _address **)**

**Parameters:**
* **_address_**[str]: _A valid Bitcoin address._

**Returns:**
* [bool]: _Returns `True` if address is in P2SH format._

---------

**oogway.validate.is_bech32(** _address **)**

**Parameters:**
* **_address_**[str]: _A valid Bitcoin address._

**Returns:**
* [bool]: _Returns `True` if address is in Bech32 format._

---------

**oogway.validate.is_valid_address(** _address **)**

**Parameters:**
* **_address_**[str]: _A Bitcoin address._

**Returns:**
* [bool]: _Returns `True` if address is valid (regardless of format)._

---------

**oogway.validate.address_format(** _address **)**

**Parameters:**
* **_address_**[str]: _A valid Bitcoin address._

**Returns:**
* [str]: _Returns the address format._