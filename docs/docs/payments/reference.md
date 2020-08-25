---
title: Reference
---

# Payment requests reference

## Requests

**oogway.request_payment(** address, amount, exp=0, message="" **)**

**Parameters:**
* **address**[str]: _Address of the payee in a valid format._

* **amount**[int]: _Amount in Satoshi._

* **exp**[int]: _Request expiration in minutes._

* **message**[str]: _Message attached to the request._

**Returns:**
* [str]: _Payment request URI._
