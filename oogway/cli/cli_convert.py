import click
from oogway.convert import convert

@click.command()
@click.argument('btc', nargs=1)
def convert_to_satoshi(btc):
    """convert from BTC to satoshi"""
    conv = convert.to_satoshi(btc, string=True)
    click.echo('\n%s BTC is %s Satoshi\n' % (btc, conv))

@click.command()
@click.argument('satoshi', nargs=1)
def convert_to_btc(satoshi):
    """convert from satoshi to BTC"""
    conv = convert.to_btc(satoshi, string=True)
    click.echo('\n%s Satoshi is %s BTC\n' % (satoshi, conv))
