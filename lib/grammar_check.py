
def check_grammar(text):
    if (text[0].isupper()) and text.endswith(('!', '?', '.')):
        return 'Well done, your grammar is correct!'
    else:
        return "Please re-check your grammar."


