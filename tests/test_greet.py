from lib.greet import *

def test_greet():
    result =  greet('Ledia')
    assert result == 'Hello, Ledia!'