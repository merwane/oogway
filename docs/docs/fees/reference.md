---
title: Reference
---

# Fees reference

## Fees

**oogway.get_fees(** timeframe="fastest", provider="blockstream" **)**

**Parameters:**
* **timeframe**[str]: _Timeframe for confirmation in blocks._ (`fastest`, `3`, `6`)
* **provider**[str]: _Transaction fees estimation provider._ Set to Blockstream by default.
 
**Returns:**
* [int]: _Estimated fees in Satoshis/byte_
