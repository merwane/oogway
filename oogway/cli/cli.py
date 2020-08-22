import click
from oogway.cli.cli_address import keypair, validate
from oogway.cli.cli_convert import convert_to_satoshi, convert_to_btc

@click.group(invoke_without_command=True)
def cli():
    pass

cli.add_command(keypair)
cli.add_command(validate)
cli.add_command(convert_to_satoshi)
cli.add_command(convert_to_btc)
