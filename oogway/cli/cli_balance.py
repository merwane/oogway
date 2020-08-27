import click
from oogway.net import Net
from oogway.convert import convert

@click.command()
@click.argument('addresses', nargs=-1)
@click.option('--network', default="mainnet", help="Network (mainnet | testnet)")
def balance(addresses, network):
    """Get addresses balance"""
    n = Net(provider="blockstream", network=network)
    
    for address in addresses:
        bal_sat = n.balance(address)
        bal_btc = convert.to_btc(bal_sat, string=True)

        click.echo("\n[%s] %s Satoshis (%s BTC)\n" % (address, bal_sat, bal_btc))
