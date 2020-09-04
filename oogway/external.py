import requests
from .exceptions import ApiError
from .convert import convert
from .utils.crypto import bytes_to_hex
from .tx import address_to_scriptpubkey
from .utils.meta import Unspent

class Blockchair:
    """retrieve blockchain data using the Blockchair API"""
    def __init__(self, network='mainnet'):
        network = network.lower()
        if network == 'mainnet':
            self.endpoint = "https://api.blockchair.com/bitcoin/"
        elif network == 'testnet':
            self.endpoint = "https://api.blockchair.com/bitcoin/testnet/"
        else:
            raise ValueError("Network unrecognized")

        self.address_info = "dashboards/address/{}"
        self.tx_info = "raw/transaction/{}"
        self.push_tx = "push/transaction"
        self.network = network

    def balance(self, address, unit='satoshi'):
        """get address balance"""
        endpoint = self.endpoint + self.address_info
        r = requests.get(endpoint.format(address))
        if r.status_code != 200:
            raise ApiError("Blockchair API unreachable")
        
        bal = r.json()['data'][address]['address']['balance']
        unit = unit.lower()
        if unit == 'satoshi':
            bal = int(bal)
        elif unit == 'btc':
            bal = convert.to_btc(bal)
        else:
            raise ValueError("Unit %s does not exist" % unit)

        return bal
    
    def txs(self, address):
        """get transaction hashes"""
        endpoint = self.endpoint + self.address_info
        params = {'offset': '0', 'limit': '1000'}
        r = requests.get(endpoint.format(address), params=params)
        if r.status_code != 200:
            raise ApiError("Blockchair API unreachable")

        transactions = r.json()['data'][address]['transactions']
        
        return transactions
    
    def utxo(self, address):
        """get unspents"""
        endpoint = self.endpoint + self.address_info
        params = {'offset': '0', 'limit': '1000'}
        r = requests.get(endpoint.format(address), params=params)
        if r.status_code != 200:
            raise ApiError("Blockchair API unreachable")

        res = r.json()

        block_height = res['context']['state']
        response = res['data'][address]
        script_pubkey = response['address']['script_hex']
        total_utxo = response['address']['unspent_output_count']
        utxos = response['utxo']
        _utxo = []
        
        for unspent in utxos:
            if unspent['block_id'] == -1:
                confs = 0
            else:
                confs = (block_height - unspent['block_id']) + 1
            _utxo.append({
                "value": unspent['value'],
                "confirmations": confs,
                "script": script_pubkey,
                "hash": unspent['transaction_hash'],
                "index": unspent['index']
                })

        return _utxo


class Blockstream:
    """retrieve blockchain data using the Blockstream API"""
    def __init__(self, network='mainnet'):
        network = network.lower()
        if network == "mainnet":
            self.endpoint = "https://blockstream.info/api/"
        elif network == "testnet":
            self.endpoint = "https://blockstream.info/testnet/api/"
        else:
            raise ValueError("Network unrecognized")
    
        self.address_info = "address/{}"
        self.tx_info = "tx/{}/hex"
        self.push_tx = "tx"
        self.unspent = "/utxo"
        self.network = network

    def balance(self, address, unit='satoshi'):
        """get address balance"""
        endpoint = self.endpoint + self.address_info
        r = requests.get(endpoint.format(address))
        if r.status_code != 200:
            raise ApiError("Blockstream API unreachable")
        
        r = r.json()
        funded = r['chain_stats']['funded_txo_sum'] + r['mempool_stats']['funded_txo_sum']
        spent = r['chain_stats']['spent_txo_sum'] + r['mempool_stats']['spent_txo_sum']

        bal = funded - spent

        unit = unit.lower()
        if unit == "satoshi":
            bal = int(bal)
        elif unit == "btc":
            bal = convert.to_btc(bal)
        else:
            raise ValueError("Unit %s does not exist" % unit)

        return bal

    def txs(self, address):
        """get transaction hashes"""
        endpoint = self.endpoint + self.address_info + '/txs/chain/{}'
        mempool_endpoint = self.endpoint + self.address_info + '/txs/mempool'

        transactions = []

        r = requests.get(mempool_endpoint.format(address))
        if r.status_code == 400:
            return []
        elif r.status_code != 200:
            raise ApiError("Blockstream API unreachable")

        response = r.json()
        unconfirmed = [tx['txid'] for tx in response]
        if len(unconfirmed) == 50:
            raise ApiError("Operation unsafe. Too many unconfirmed transactions.")

        r = requests.get(endpoint.format(address, ''))
        if r.status_code == 400:
            return []
        elif r.status_code != 200:
            raise ApiError("Blockstream API unreachable")

        response = r.json()

        total_txs = len(response)

        while total_txs > 0:
            transactions.extend(tx['txid'] for tx in response)

            response = requests.get(endpoint.format(address, transactions[-1])).json()
            total_txs = len(response)

        transactions.extend(unconfirmed)

        return transactions
    
    def utxo(self, address):
        """get unspents"""
        endpoint = self.endpoint + 'blocks/tip/height'
        r_block = requests.get(endpoint)
        if r_block.status_code != 200:
            raise ApiError("Blockstream API unreachable")

        block_height = int(r_block.text)

        utxo_endpoint = (self.endpoint+self.address_info+self.unspent).format(address)
        r = requests.get(utxo_endpoint)
        if r.status_code == 400 and r.text == "Too many history entries":
            raise ApiError("Excessive address")
        elif r.status_code != 200:
            raise ApiError("Blockstream API unreachable")

        script_pubkey = bytes_to_hex(address_to_scriptpubkey(address))
        return sorted(
            [
                Unspent(
                    tx["value"],
                    block_height - tx["status"]["block_height"] + 1 if tx["status"]["confirmed"] else 0,
                    script_pubkey,
                    tx["txid"],
                    tx["vout"],
                )
                for tx in r.json()
            ],
            key=lambda u: u.confirmations,
        )

    def broadcast(self, tx_hex):
        endpoint = self.endpoint + self.push_tx
        r = requests.post(endpoint, data=tx_hex)
        return True if r.status_code == 200 else False