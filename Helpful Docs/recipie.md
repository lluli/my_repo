## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def reading_time(text):
parameters - the text to be read (float as it might not be exact)
returns - amount of time needed to read text 
side effects - the function doesnt print anything if there is no text 

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

given 200 words
reading_time('200') 
==> 1.0

given 400 words 
reading_time('400') 
==> 2.0

given 300 words 
reading_time('600') 
==> 1.5

given 700 words
reading_time('700')
==> 3.5

given 0 words 
reading_time('')
==> 'No text added!'



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._



```python
def reading_time(text):
    words = text.split()
    amount_of_words = len(words) 
    reading_time = amount_of_words / 200 
    return reading_time
