def test_key_module():
    try:
        from oogway import Key
        imported = True
    except ImportError:
        imported = False

    assert imported == True

def test_validate_module():
    try:
        from oogway import validate
        imported = True
    except ImportError:
        imported = False
    
    assert imported == True

def test_convert_module():
    try:
        from oogway import convert
        imported = True
    except ImportError:
        imported = False
    
    assert imported == True

def test_operation_module():
    try:
        from oogway import operation
        imported = True
    except ImportError:
        imported = False

    assert imported == True

def test_fees_module():
    try:
        from oogway import get_fees
        imported = True
    except ImportError:
        imported = False

    assert imported == True

def test_request_module():
    try:
        from oogway import request_payment, parse_request
        imported = True
    except ImportError:
        imported = False

    assert imported == True
