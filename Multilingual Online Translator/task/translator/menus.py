from data import TranslationData

LANGUAGES = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew',
             'japanese', 'dutch', 'polish', 'portuguese', 'romanian',
             'russian', 'turkish']


class Menus:
    def __init__(self):
        ...

    @staticmethod
    def welcome():
        print('Hello, welcome to the translator. Translator supports: ')
        print(*(f'{i}. {lang.capitalize()}' for i, lang
                in enumerate(LANGUAGES, start=1)), sep='\n')

    def choose_first_lang(self) -> str:
        return self._choose_lang('Type the number of your language:\n')

    def choose_second_lang(self) -> str:
        return self._choose_lang('Type the number of language you want '
                                 'to translate to:\n')

    @staticmethod
    def _choose_lang(text: str) -> str:
        return LANGUAGES[-1 + int(input(text))]

    @staticmethod
    def choose_word() -> str:
        return input('Type the word you want to translate:\n')
