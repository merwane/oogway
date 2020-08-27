from .external import Blockchair, Blockstream

class Net:
    def __init__(self, provider='blockstream', network='mainnet'):
        provider = provider.lower()
        if provider == 'blockchair':
            self.provider = Blockchair(network=network)
        elif provider == "blockstream":
            self.provider = Blockstream(network=network)
        else:
            raise ValueError("Invalid provider")

    def balance(self, address, unit='satoshi'):
        r = self.provider.balance(address, unit)
        return r

    def txs(self, address):
        r = self.provider.txs(address)
        return r

    def utxo(self, address):
        if self.provider == "blockstream":
            raise ValueError("Retrieving UTXO from Blockstream unsupported. Use Blockchair.")
        r = self.provider.utxo(address)
        return r
