class GrammarStats:
    def __init__(self):
        self.correct = 0
        self.total = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper() and text.endswith(('!', '?', '.')):
            self.total += 1
            self.correct += 1
            return True
        else:
            self.total += 1 
            return False

    def percentage_good(self):
        percentage = ((self.correct/self.total) * 100)
        return f"{percentage}%"
