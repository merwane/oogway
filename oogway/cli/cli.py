import click
from oogway.cli.cli_address import keypair, validate
from oogway.cli.cli_convert import convert_to_satoshi, convert_to_btc
from oogway.cli.cli_fees import fees
from oogway.cli.cli_request import request_payment
from oogway.cli.cli_balance import balance
from oogway.cli.cli_broadcast import broadcast

@click.group(invoke_without_command=True)
def cli():
    pass

cli.add_command(keypair)
cli.add_command(validate)
cli.add_command(convert_to_satoshi)
cli.add_command(convert_to_btc)
cli.add_command(fees)
cli.add_command(request_payment)
cli.add_command(balance)
cli.add_command(broadcast)
