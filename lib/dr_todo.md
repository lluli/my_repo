# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

''''
As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.
'''

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_if_todo_in_text(text):
    return '#TODO in text!'

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given text had #TODO in it 
Return sucess message
"""

check_if_todo_in_text('#TODO washing') => '#TODO in text!'

"""
Given text does not have #TODO in it 
Return failed message
"""

check_if_todo_in_text('bins') => '#TODO not in text!'


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
