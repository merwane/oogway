import click
from oogway.request import request_payment as reqp

@click.command()
@click.argument('address', nargs=1)
@click.argument('amount', nargs=1)
@click.option('--expire', default=0, help="payment request expiration in minutes")
@click.option('--message', default="", help="message")
def request_payment(address, amount, expire, message):
    request = reqp(address, amount, expire, message)
    click.echo('\n%s\n' % request)
