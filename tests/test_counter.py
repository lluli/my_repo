from lib.counter import *

def test_counter_report_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_a_single_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."    