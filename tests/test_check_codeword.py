from lib.check_codeword import *

def test_check_codeword():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

    result = check_codeword('hose')
    assert result == "Close, but nope."

    result = check_codeword('Ping')
    assert result == "WRONG!"