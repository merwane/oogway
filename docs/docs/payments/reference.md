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

-----------------

**oogway.parse_request(** uri **)**

**Parameters:**

* **uri**[str]: _Valid Bitcoin payment URI._

**Returns:**

* [dict]: 
    * **address**[str]: _Bitcoin address._
    * **amount**[str]: _Requested amount in Satoshi._
    * **created**[str]: _Date of creation._
    * **status**[str]: _Current status._ (valid | expired)
    * **exp**[str]: _Expiration time in seconds._
    * **message**[str]: _Attached message._