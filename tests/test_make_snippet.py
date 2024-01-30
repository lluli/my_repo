from lib.make_snippet import *

"""
given an empty string, 
an empty string is returned 
"""

def test_given_an_empty_string_returns_an_empty_string():
    result = make_snippet("")
    assert result == ""

def test_given_a_string_five_and_under_returns_the_string():
    result = make_snippet('I love Athi so much')
    assert result == 'I love Athi so much'

def test_given_a_string_five_or_over_returns_the_string_and_dotdotdots():
    result = make_snippet('I love Athi so much it hurts')
    assert result == 'I love Athi so much...'