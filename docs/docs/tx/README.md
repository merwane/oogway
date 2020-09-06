---
title: Transaction
---

# Transaction

The transaction method can be used for creating, signing and broadcasting Bitcoin transactions. The current implementation is a fork of [Ofek's](https://github.com/ofek/bit).

## Create then broadcast a transaction

Create and sign a transaction, return it in raw (`hex`) format and broadcast it at any time:

```python
>>> from oogway import Tx, Net, Node
>>> wif = "5JmFZgAQCpAMwxpqmGeTjf9y1egjMfbJgtsmNA9FSUPXA55KyqW"
>>> tx = Tx(wif, network="mainnet")
>>> outputs = [('1FHXDkRLhoCziRjftaPB3fELUYrZomFanx', 100000)] # 100000 sats
>>> tx_hex = tx.create_transaction(outputs)
>>>
>>> # Broadcast later using your node
>>> node = Node("http://username:password@host:port")
>>> node.sendrawtransaction(tx_hex)
>>>
>>> # or the Blockstream API
>>> net = Net()
>>> net.broadcast(tx_hex)
```

## Send a transaction

Create, sign and broadcast a transaction in one operation:

```python
>>> from oogway import Tx
>>> wif = "5JmFZgAQCpAMwxpqmGeTjf9y1egjMfbJgtsmNA9FSUPXA55KyqW"
>>> tx = Tx(wif, network="mainnet")
>>> outputs = [('1FHXDkRLhoCziRjftaPB3fELUYrZomFanx', 100000)] # 100000 sats
>>> tx.send(outputs)
'5f98ce3f4e65a79f3eeed6179898e4f355f0883a5b83bfb9aabac4154a5b0108'
```