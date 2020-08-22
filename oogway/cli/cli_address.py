import click
from oogway.key import Key
from oogway.validate import validate as validation

@click.command()
@click.option('--address', default='bech32', help="address format (Bech32 | P2SH | P2PKH)")
@click.option('--testnet', default=False, help="generate testnet keypair (True | False)")
def keypair(address, testnet):
    """generates keypair with specific address format"""
    key = Key(testnet=testnet, mnemonic_strength=128)
       
    address = address.lower()

    if address == 'bech32':
        _address = key.address(address)
    elif address == 'p2sh':
        _address = key.address(address)
    elif address == 'p2pkh':
        _address = key.address(address)
    else:
        raise click.BadParameter('Invalid address format passed', param_hint=["--address"])
    
    click.echo('\n------------------------------------')
    click.echo('MNEMONIC: %s' % key.mnemonic)
    click.echo('WIF: %s' % key.wif)
    click.echo('ADDRESS: %s' % _address)
    click.echo('------------------------------------\n')

@click.command()
@click.argument('addresses', nargs=-1)
def validate(addresses):
    """validate a set of addresses and returns format"""
    for address in addresses:
        v = validation.is_valid_address(address)
        try:
            _format = validation.address_format(address)
        except ValueError:
            _format = "INVALID"
        if v == True:
            click.echo('\n[VALID | %s] %s\n' % (_format, address))
        elif v == False:
            click.echo('\n[INVALID] %s\n' % address)
