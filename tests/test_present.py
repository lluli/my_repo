import pytest 
from lib.present import * 

def test_wrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap () == 33

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."