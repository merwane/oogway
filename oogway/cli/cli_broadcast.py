import click
from oogway.net import Net
from oogway.tx import calc_txid

@click.command()
@click.option('--network', default='mainnet', help="Broadcasts transaction on selected network (mainnet | testnet)")
@click.argument('tx_hex', nargs=1)
def broadcast(network, tx_hex):
    n = Net(network=network)
    tx_hash = n.broadcast(tx_hex)

    if tx_hash == False:
        click.echo('\nTransaction failed to broadcast.\n')
    elif tx_hash == True:
        txid = calc_txid(tx_hex)
        click.echo('\nTransaction broadcasted: %s\n' % txid)
