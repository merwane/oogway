"""
Copyright (c) 2016 Ofek Lev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import json
from .utils.crypto import ECPrivateKey, ripemd160_sha256, sha256
from .utils.curve import Point
from .utils.format import (
    bytes_to_wif,
    public_key_to_address,
    public_key_to_coords,
    wif_to_bytes,
    multisig_to_address,
    multisig_to_redeemscript,
    public_key_to_segwit_address,
    multisig_to_segwit_address
)
from .net import Net
from .fees import get_fees
from .tx import (
    calc_txid,
    create_new_transaction,
    sanitize_tx_data,
    sign_tx,
    deserialize,
    address_to_scriptpubkey,
)
from .utils.opcodes import OP_0, OP_PUSH_20, OP_PUSH_32
from .utils.utils import hex_to_bytes, bytes_to_hex, int_to_varint
from .key import Key

class BaseKey:
    """This class represents a point on the elliptic curve secp256k1 and
    provides all necessary cryptographic functionality. You shouldn't use
    this class directly.
    :param wif: A private key serialized to the Wallet Import Format. If the
                argument is not supplied, a new private key will be created.
                The WIF compression flag will be adhered to, but the version
                byte is disregarded. Compression will be used by all new keys.
    :type wif: ``str``
    :raises TypeError: If ``wif`` is not a ``str``.
    """

    def __init__(self, wif=None):
        if wif:
            if isinstance(wif, str):
                private_key_bytes, compressed, version = wif_to_bytes(wif)
                self._pk = ECPrivateKey(private_key_bytes)
            elif isinstance(wif, ECPrivateKey):
                self._pk = wif
                compressed = True
            else:
                raise TypeError('Wallet Import Format must be a string.')
        else:
            self._pk = ECPrivateKey()
            compressed = True

        self._public_point = None
        self._public_key = self._pk.public_key.format(compressed=compressed)

    @property
    def public_key(self):
        """The public point serialized to bytes."""
        return self._public_key

    @property
    def public_point(self):
        """The public point (x, y)."""
        if self._public_point is None:
            self._public_point = Point(*public_key_to_coords(self._public_key))
        return self._public_point

    def sign(self, data):
        """Signs some data which can be verified later by others using
        the public key.
        :param data: The message to sign.
        :type data: ``bytes``
        :returns: A signature compliant with BIP-62.
        :rtype: ``bytes``
        """
        return self._pk.sign(data)

    def verify(self, signature, data):
        """Verifies some data was signed by this private key.
        :param signature: The signature to verify.
        :type signature: ``bytes``
        :param data: The data that was supposedly signed.
        :type data: ``bytes``
        :rtype: ``bool``
        """
        return self._pk.public_key.verify(signature, data)

    def pub_to_hex(self):
        """:rtype: ``str`` """
        return bytes_to_hex(self.public_key)

    def to_hex(self):
        """:rtype: ``str``"""
        return self._pk.to_hex()

    def to_bytes(self):
        """:rtype: ``bytes``"""
        return self._pk.secret

    def to_der(self):
        """:rtype: ``bytes``"""
        return self._pk.to_der()

    def to_pem(self):
        """:rtype: ``bytes``"""
        return self._pk.to_pem()

    def to_int(self):
        """:rtype: ``int``"""
        return self._pk.to_int()

    def is_compressed(self):
        """Returns whether or not this private key corresponds to a compressed
        public key.
        :rtype: ``bool``
        """
        return True if len(self.public_key) == 33 else False

    def __eq__(self, other):
        return self.to_int() == other.to_int()


class PrivateKey(BaseKey):
    """This class represents a Bitcoin private key. ``Key`` is an alias.
    :param wif: A private key serialized to the Wallet Import Format. If the
                argument is not supplied, a new private key will be created.
                The WIF compression flag will be adhered to, but the version
                byte is disregarded. Compression will be used by all new keys.
    :type wif: ``str``
    :raises TypeError: If ``wif`` is not a ``str``.
    """

    def __init__(self, wif=None, network="mainnet"):
        super().__init__(wif=wif)

        if network == "mainnet":
            self.version = 'main'
            self.instance = 'PrivateKey'
        else:
            self.version = 'test'
            self.instance = 'PrivateKeyTestnet'

        self.network = network

        self._address = None
        self._segwit_address = None
        self._scriptcode = None
        self._segwit_scriptcode = None

        self.balance = 0
        self.unspents = []
        self.transactions = []

    @property
    def address(self):
        """The public address you share with others to receive funds."""
        if self._address is None:
            self._address = public_key_to_address(self._public_key, version=self.version)
        return self._address

    @property
    def segwit_address(self):
        """The public segwit nested in P2SH address you share with others to
        receive funds."""
        # Only make segwit address if public key is compressed
        if self._segwit_address is None and self.is_compressed():
            self._segwit_address = public_key_to_segwit_address(self._public_key, version=self.version)
        return self._segwit_address

    @property
    def scriptcode(self):
        self._scriptcode = address_to_scriptpubkey(self.address)
        return self._scriptcode

    @property
    def segwit_scriptcode(self):
        self._segwit_scriptcode = OP_0 + OP_PUSH_20 + ripemd160_sha256(self.public_key)
        return self._segwit_scriptcode

    def can_sign_unspent(self, unspent):
        script = bytes_to_hex(address_to_scriptpubkey(self.address))
        if self.segwit_address:
            segwit_script = bytes_to_hex(address_to_scriptpubkey(self.segwit_address))
            return unspent.script == script or unspent.script == segwit_script
        else:
            return unspent.script == script

    def to_wif(self):
        return bytes_to_wif(self._pk.secret, version=self.version, compressed=self.is_compressed())

    def balance_as(self, currency):
        """Returns your balance as a formatted string in a particular currency.
        :param currency: One of the :ref:`supported currencies`.
        :type currency: ``str``
        :rtype: ``str``
        """
        return self.balance

    def get_balance(self, currency='satoshi'):
        """Fetches the current balance by calling
        :func:`~bit.PrivateKey.get_unspents` and returns it using
        :func:`~bit.PrivateKey.balance_as`.
        :param currency: One of the :ref:`supported currencies`.
        :type currency: ``str``
        :rtype: ``str``
        """
        self.get_unspents()
        return self.balance_as(currency)

    def get_unspents(self):
        """Fetches all available unspent transaction outputs.
        :rtype: ``list`` of :class:`~bit.network.meta.Unspent`
        """
        self.unspents[:] = list(
            map(
                lambda u: u.set_type('p2pkh' if self.is_compressed() else 'p2pkh-uncompressed'),
                Net(network=self.network).utxo(self.address),
            )
        )
        if self.segwit_address:
            self.unspents += list(map(lambda u: u.set_type('np2wkh'), Net(network=self.network).utxo(self.address)))
        self.balance = sum(unspent.amount for unspent in self.unspents)
        return self.unspents

    def get_transactions(self):
        """Fetches transaction history.
        :rtype: ``list`` of ``str`` transaction IDs
        """
        self.transactions[:] = Net(network=self.network).txs(self.address)
        if self.segwit_address:
            self.transactions += Net(network=self.network).txs(self.address)
        return self.transactions

    def create_transaction(
        self,
        outputs,
        fee=None,
        absolute_fee=False,
        leftover=None,
        combine=True,
        message=None,
        unspents=None,
        message_is_hex=False,
        replace_by_fee=False
    ):  # pragma: no cover
        """Creates a signed P2PKH transaction.
        :param outputs: A sequence of outputs you wish to send in the form
                        ``(destination, amount, currency)``. The amount can
                        be either an int, float, or string as long as it is
                        a valid input to ``decimal.Decimal``. The currency
                        must be :ref:`supported <supported currencies>`.
        :type outputs: ``list`` of ``tuple``
        :param fee: The number of satoshi per byte to pay to miners. By default
                    Bit will poll `<https://bitcoinfees.earn.com>`_ and use a fee
                    that will allow your transaction to be confirmed as soon as
                    possible.
        :type fee: ``int``
        :param leftover: The destination that will receive any change from the
                         transaction. By default Bit will send any change to
                         the same address you sent from.
        :type leftover: ``str``
        :param combine: Whether or not Bit should use all available UTXOs to
                        make future transactions smaller and therefore reduce
                        fees. By default Bit will consolidate UTXOs. Note: When
                        setting :param absolute_fee: this is ignored.
        :type combine: ``bool``
        :param message: A message to include in the transaction. This will be
                        stored in the blockchain forever. Due to size limits,
                        each message will be stored in chunks of 40 bytes.
        :type message: ``str``
        :param unspents: The UTXOs to use as the inputs. By default Bit will
                         communicate with the blockchain itself.
        :type unspents: ``list`` of :class:`~bit.network.meta.Unspent`
        :param replace_by_fee: Whether to opt-in for replace-by-fee (BIP 125).
        :type replace_by_fee: ``bool``
        :returns: The signed transaction as hex.
        :rtype: ``str``
        """
        try:
            unspents = unspents or self.get_unspents()
        except ConnectionError:
            raise ConnectionError('All APIs are unreachable. Please provide the unspents to spend from directly.')

        # If at least one input is from segwit the return address is for segwit
        return_address = self.segwit_address if any([u.segwit for u in unspents]) else self.address

        unspents, outputs = sanitize_tx_data(
            unspents,
            outputs,
            (fee or get_fees()) if self.network == "mainnet" else 2,
            leftover or return_address,
            combine=combine,
            message=message,
            absolute_fee=absolute_fee,
            version=self.version,
            message_is_hex=message_is_hex,
            replace_by_fee=replace_by_fee
        )

        return create_new_transaction(self, unspents, outputs)

    def send(
        self,
        outputs,
        fee=None,
        absolute_fee=False,
        leftover=None,
        combine=True,
        message=None,
        unspents=None,
        message_is_hex=False,
        replace_by_fee=False
    ):  # pragma: no cover
        """Creates a signed P2PKH transaction and attempts to broadcast it on
        the blockchain. This accepts the same arguments as
        :func:`~bit.PrivateKey.create_transaction`.
        :param outputs: A sequence of outputs you wish to send in the form
                        ``(destination, amount, currency)``. The amount can
                        be either an int, float, or string as long as it is
                        a valid input to ``decimal.Decimal``. The currency
                        must be :ref:`supported <supported currencies>`.
        :type outputs: ``list`` of ``tuple``
        :param fee: The number of satoshi per byte to pay to miners. By default
                    Bit will poll `<https://bitcoinfees.earn.com>`_ and use a fee
                    that will allow your transaction to be confirmed as soon as
                    possible.
        :type fee: ``int``
        :param leftover: The destination that will receive any change from the
                         transaction. By default Bit will send any change to
                         the same address you sent from.
        :type leftover: ``str``
        :param combine: Whether or not Bit should use all available UTXOs to
                        make future transactions smaller and therefore reduce
                        fees. By default Bit will consolidate UTXOs. Note: When
                        setting :param absolute_fee: this is ignored.
        :type combine: ``bool``
        :param message: A message to include in the transaction. This will be
                        stored in the blockchain forever. Due to size limits,
                        each message will be stored in chunks of 40 bytes.
        :type message: ``str``
        :param unspents: The UTXOs to use as the inputs. By default Bit will
                         communicate with the blockchain itself.
        :type unspents: ``list`` of :class:`~bit.network.meta.Unspent`
        :param replace_by_fee: Whether to opt-in for replace-by-fee (BIP 125).
        :type replace_by_fee: ``bool``
        :returns: The transaction ID.
        :rtype: ``str``
        """

        tx_hex = self.create_transaction(
            outputs,
            fee=(fee or get_fees()) if self.network == "mainnet" else 2,
            absolute_fee=absolute_fee,
            leftover=leftover,
            combine=combine,
            message=message,
            unspents=unspents,
            message_is_hex=message_is_hex,
            replace_by_fee=replace_by_fee
        )

        Net(network=self.network).broadcast(tx_hex)

        return calc_txid(tx_hex)

    @classmethod
    def prepare_transaction(
        cls,
        address,
        outputs,
        compressed=True,
        fee=None,
        absolute_fee=False,
        leftover=None,
        combine=True,
        message=None,
        unspents=None,
        message_is_hex=False,
        replace_by_fee=False
    ):  # pragma: no cover
        """Prepares a P2PKH transaction for offline signing.
        :param address: The address the funds will be sent from.
        :type address: ``str``
        :param outputs: A sequence of outputs you wish to send in the form
                        ``(destination, amount, currency)``. The amount can
                        be either an int, float, or string as long as it is
                        a valid input to ``decimal.Decimal``. The currency
                        must be :ref:`supported <supported currencies>`.
        :type outputs: ``list`` of ``tuple``
        :param compressed: Whether or not the ``address`` corresponds to a
                           compressed public key. This influences the fee.
        :type compressed: ``bool``
        :param fee: The number of satoshi per byte to pay to miners. By default
                    Bit will poll `<https://bitcoinfees.earn.com>`_ and use a fee
                    that will allow your transaction to be confirmed as soon as
                    possible.
        :type fee: ``int``
        :param leftover: The destination that will receive any change from the
                         transaction. By default Bit will send any change to
                         the same address you sent from.
        :type leftover: ``str``
        :param combine: Whether or not Bit should use all available UTXOs to
                        make future transactions smaller and therefore reduce
                        fees. By default Bit will consolidate UTXOs. Note: When
                        setting :param absolute_fee: this is ignored.
        :type combine: ``bool``
        :param message: A message to include in the transaction. This will be
                        stored in the blockchain forever. Due to size limits,
                        each message will be stored in chunks of 40 bytes.
        :type message: ``str``
        :param unspents: The UTXOs to use as the inputs. By default Bit will
                         communicate with the blockchain itself.
        :type unspents: ``list`` of :class:`~bit.network.meta.Unspent`
        :param replace_by_fee: Whether to opt-in for replace-by-fee (BIP 125).
        :type replace_by_fee: ``bool``
        :returns: JSON storing data required to create an offline transaction.
        :rtype: ``str``
        """
        unspents, outputs = sanitize_tx_data(
            unspents or Net(network=self.network).utxo(address),
            outputs,
            (fee or get_fees()) if self.network == "mainnet" else 2,
            leftover or address,
            combine=combine,
            message=message,
            absolute_fee=absolute_fee,
            version='main',
            message_is_hex=message_is_hex,
            replace_by_fee=replace_by_fee
        )

        data = {'unspents': [unspent.to_dict() for unspent in unspents], 'outputs': outputs}

        return json.dumps(data, separators=(',', ':'))

    def sign_transaction(self, tx_data, unspents=None):  # pragma: no cover
        """Creates a signed P2PKH transaction using previously prepared
        transaction data.
        :param tx_data: Hex-encoded transaction or output of :func:`~bit.Key.prepare_transaction`.
        :type tx_data: ``str``
        :param unspents: The UTXOs to use as the inputs. By default Bit will
                         communicate with the blockchain itself.
        :type unspents: ``list`` of :class:`~bit.network.meta.Unspent`
        :returns: The signed transaction as hex.
        :rtype: ``str``
        """
        try:  # Json-tx-data from :func:`~bit.Key.prepare_transaction`
            data = json.loads(tx_data)
            assert unspents is None

            unspents = [Unspent.from_dict(unspent) for unspent in data['unspents']]
            outputs = data['outputs']

            return create_new_transaction(self, unspents, outputs)
        except:  # May be hex-encoded transaction using batching:
            try:
                unspents = unspents or self.get_unspents()
            except ConnectionError:
                raise ConnectionError(
                    'All APIs are unreachable. Please provide the unspent '
                    'inputs as unspents directly to sign this transaction.'
                )

            tx_data = deserialize(tx_data)
            return sign_tx(self, tx_data, unspents=unspents)

    @classmethod
    def from_hex(cls, hexed):
        """
        :param hexed: A private key previously encoded as hex.
        :type hexed: ``str``
        :rtype: :class:`~bit.PrivateKey`
        """
        return PrivateKey(ECPrivateKey.from_hex(hexed))

    @classmethod
    def from_bytes(cls, bytestr):
        """
        :param bytestr: A private key previously encoded as hex.
        :type bytestr: ``bytes``
        :rtype: :class:`~bit.PrivateKey`
        """
        return PrivateKey(ECPrivateKey(bytestr))

    @classmethod
    def from_der(cls, der):
        """
        :param der: A private key previously encoded as DER.
        :type der: ``bytes``
        :rtype: :class:`~bit.PrivateKey`
        """
        return PrivateKey(ECPrivateKey.from_der(der))

    @classmethod
    def from_pem(cls, pem):
        """
        :param pem: A private key previously encoded as PEM.
        :type pem: ``bytes``
        :rtype: :class:`~bit.PrivateKey`
        """
        return PrivateKey(ECPrivateKey.from_pem(pem))

    @classmethod
    def from_int(cls, num):
        """
        :param num: A private key in raw integer form.
        :type num: ``int``
        :rtype: :class:`~bit.PrivateKey`
        """
        return PrivateKey(ECPrivateKey.from_int(num))

    def __repr__(self):
        return '<PrivateKey: {}>'.format(self.address)