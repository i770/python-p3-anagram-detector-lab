class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for word in word_list:
            if sorted(word.lower()) == sorted_word and word.lower() != self.word:
                matches.append(word)
                
        return matches
