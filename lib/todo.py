def check_if_todo_in_text(text):
    if '#TODO' in text:
        return '#TODO in text!'
    else:
        return '#TODO not in text!'