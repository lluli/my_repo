def reading_time(text):
    words = text.split()
    amount_of_words = len(words) 
    reading_time = amount_of_words / 200 
    return reading_time