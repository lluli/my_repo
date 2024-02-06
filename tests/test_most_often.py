from lib.most_often import *

def test_most_often_with_single_item():
    most_often = MostOften(['pot noodle'])
    result = most_often.get_most_often()
    assert result == 'pot noodle'

def test_most_often_with_two_items():
    most_often = MostOften(['pot noodle', 'super noodle'])
    result = most_often.get_most_often()
    assert result == "no clear winner"

def test_most_often_with_three_items():
    most_often = MostOften(['pot noodle', 'super noodle', 'pot noodle'])
    result = most_often.get_most_often()
    assert result == 'pot noodle'