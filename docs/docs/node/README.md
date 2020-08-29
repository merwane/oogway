---
title: Node
---

# Node

The node method can be used for interacting with your own Bitcoin node via the json RPC interface. The list of all available calls can be found [here](https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list).

## Get longest chain

Returns the current number of blocks in the Bitcoin blockchain:

```python
>>> from oogway import Node
>>> node = Node("http://username:password@host:port")
>>> node.getblockcount()
645914
```

## Get the hash of the genesis block

Returns the block hash given a block index:

```python
>>> from oogway import Node
>>> node = Node("http://username:password@host:port")
>>> node.getblockhash(0)
'000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
```