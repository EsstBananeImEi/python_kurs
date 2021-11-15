class Speak(object):
    def __init__(self, list_with_words):
        self.list_with_words = list_with_words
        self.current_index = 0

    def set_next_index(self):
        if self.current_index < len(self.list_with_words) - 1:
            self.current_index = self.current_index + 1
        else:
            self.current_index = 0

    def get_word(self):
        return self.list_with_words[self.current_index]

    def set_word(self, word):
        self.current_index = self.list_with_words.index(word)


a = Speak(["gut", "Morgen", "Wurst", "Blitz", "Geist", "Volk", "Nacht", "Hund"])
a.set_word('Morgen')
print(a.get_word())
for i in range(len(a.list_with_words)):
    a.set_next_index()
    print(a.get_word())
