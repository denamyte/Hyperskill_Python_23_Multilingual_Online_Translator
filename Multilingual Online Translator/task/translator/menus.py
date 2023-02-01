import dataclasses

from data import TranslationData, TranslationResult


class Menus:
    def __init__(self):
        self._lang_to = ''
        self._word = ''

    def choose_lang(self) -> str:
        self._lang_to = input(
            'Type "en" if you want to translate from French into English,'
            ' or "fr" if you want to translate from English into French:\n')

    def choose_word(self) -> str:
        self._word = input('Type the word you want to translate:\n')

    def confirm_chosen(self):
        print(f'You chose "{self._lang_to}" as the language to translate "{self._word}" to.')

    @staticmethod
    def confirm_query():
        print('200 OK')

    @property
    def data(self) -> TranslationData:
        """ Returns the translation data (language, word) """
        lang_from = 'en' if self._lang_to == 'fr' else 'fr'
        return TranslationData(lang_from, self._lang_to, self._word)
