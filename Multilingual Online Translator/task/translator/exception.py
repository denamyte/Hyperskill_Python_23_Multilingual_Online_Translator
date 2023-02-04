class LanguageNotSupportedError(Exception):
    def __init__(self, lang: str):
        self.lang = lang

    def __str__(self):
        return "Sorry, the program doesn't support " + self.lang


class InternetConnectionError(Exception):
    def __str__(self):
        return 'Something wrong with your internet connection'


class CannotFindWordError(Exception):
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return 'Sorry, unable to find ' + self.word
