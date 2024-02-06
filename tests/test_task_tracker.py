from lib.task_tracker import *

""" Test adding one task"""
def test_add_one_task():
    task_tracker = TaskTracker()
    task_tracker.add('Dishes')
    result = task_tracker.to_do
    assert result == ['Dishes']

def test_add_two_tasks():
    task_tracker = TaskTracker()
    task_tracker.add('Dishes')
    task_tracker.add('Laundry')
    result = task_tracker.to_do
    assert result == ['Dishes', 'Laundry']

""" Test removing one tasks"""
def test_removing_one_task():
    task_tracker = TaskTracker()
    task_tracker.add('Dishes')
    task_tracker.remove('Dishes')
    result = task_tracker.to_do
    assert result == []

















""" Test adding two tasks"""


""" Test adding five tasks"""


""" Test adding task already on list"""


""" Test removing one tasks"""


""" Test removing two tasks"""


""" Test removing task not in list"""