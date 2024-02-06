import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.read_so_far = 0 

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('Please learn to read first!')
        amount_of_words = self.count_words()
        return math.ceil(amount_of_words / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        start = self.read_so_far
        end = self.read_so_far + words_user_can_read
        chunk_of_words = words[start:end]
        self.read_so_far = end
        return " ".join(chunk_of_words)