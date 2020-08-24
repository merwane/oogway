import click
from oogway.fees import get_fees

@click.command()
@click.option('--timeframe', default='fastest', help="Timeframe for confirmation in blocks (fastest | 3 | 6)")
def fees(timeframe):
    fee = get_fees(timeframe=timeframe)
    fee = str(fee)
    click.echo('\n%s Satoshis/byte\n' % fee)
