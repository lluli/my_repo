from lib.todo import *

def test_todo_in_text():
    result = check_if_todo_in_text('#TODO washing')
    assert result == '#TODO in text!'

def test_todo_not_in_text():
    result = check_if_todo_in_text('bins')
    assert result == '#TODO not in text!'