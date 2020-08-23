---
title: Validation overview
---

# Validation

The validation methods can be used to validate Bitcoin addresses or return their format. This is useful for verifying the validity of an address before making a transaction.

`oogway.validate` validates addresses cryptographically and by using regular expressions. This ensures an optimal level of security as only using regular expressions to validate an address is dangerous.

## Validate an address

Validating a Bitcoin address using oogway only takes one line of code:

```python
>>> from oogway import validate
>>> validate.is_p2pkh("1FHXDkRLhoCziRjftaPB3fELUYrZomFanx")
True
>>> validate.is_bech32("3AAGkDZ8i5QyPEuraj8Ja79PUXPMe2QwKV")
False
```

It can also be used to validate addresses regardless of their format:
```python
>>> from oogway import validate
>>> validate.is_valid_address("bc1qs3frll3lan0v0r3xsfe8r3phrc24smn4hkmwm4")
True
>>> validate.is_valid_address("1FHXDkRLh0CzIRjftaPB3fELUYrZomFanx")
False
```

Or to detect an address format:
```python
>>> from oogway import validate
>>> validate.address_format("1FHXDkRLhoCziRjftaPB3fELUYrZomFanx")
'P2PKH'
```

## CLI

Another thing you can do is validate addresses using the CLI:

```console
$ oogway validate 1FHXDkRLhoCziRjftaPB3fELUYrZomFanx bc1qs3frll3lan0v0r3xsfe8r3phrc24smn4hkmwm4 3AAGkDZ8i50yPEurIj8Ja79PUXPMe2QwKV

[VALID | P2PKH] 1FHXDkRLhoCziRjftaPB3fELUYrZomFanx
[VALID | Bech32] bc1qs3frll3lan0v0r3xsfe8r3phrc24smn4hkmwm4
[INVALID] 3AAGkDZ8i50yPEurIj8Ja79PUXPMe2QwKV

```