---
title: Network
---

# Network

The network method can be used for interacting with Bitcoin APIs to retrieve balances, transactions and unspents. It is however advisable to retrieve these from your own node, using the [Node](/node) method.

## Get balance

Getting the balance of an address using oogway:

```python
>>> from oogway import Net
>>> n = Net(provider="Blockstream", network="mainnet")
>>> n.balance(address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", unit="satoshi")
'1832613467'
```

## CLI

You can get balances using the CLI:

```console
$ oogway balance 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa 1FHXDkRLhoCziRjftaPB3fELUYrZomFanx

> [1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa] 1832613467 Satoshis (18.32613467 BTC)
> [1FHXDkRLhoCziRjftaPB3fELUYrZomFanx] 0 Satoshi (0 BTC)
```