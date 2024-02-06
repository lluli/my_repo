from lib.grammar_check import *

def test_a_correct_sentece():
    result = check_grammar('This sentence is perfect.')
    assert result == 'Well done, your grammar is correct!'

def test_a_correct_second_sentece():
    result = check_grammar('Is this sentence perfect?')
    assert result == 'Well done, your grammar is correct!'

def test_a_correct_third_sentece():
    result = check_grammar('This is a great sentence!')
    assert result == 'Well done, your grammar is correct!'

def test_a_wrong_sentece():
    result = check_grammar('this is wrong')
    assert result == 'Please re-check your grammar.'

def test_a_wrong_second_sentece():
    result = check_grammar('this is also wrong/')
    assert result == 'Please re-check your grammar.'    