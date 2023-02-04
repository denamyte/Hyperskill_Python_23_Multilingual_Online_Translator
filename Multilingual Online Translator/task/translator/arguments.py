from argparse import ArgumentParser
from data import TranslationData
from exception import LanguageNotSupportedError

LANGUAGES = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew',
             'japanese', 'dutch', 'polish', 'portuguese', 'romanian',
             'russian', 'turkish']


def parse_args() -> TranslationData:
    parser = ArgumentParser()
    parser.add_argument('src_l')
    parser.add_argument('trg_l')
    parser.add_argument('word')
    args = parser.parse_args()
    test_lang_support(args.src_l)
    test_lang_support(args.trg_l)
    if args.trg_l == 'all':
        trg_l = LANGUAGES[:]
        if args.src_l in trg_l:
            trg_l.remove(args.src_l)
    else:
        trg_l = [args.trg_l]
    return TranslationData(args.src_l, trg_l, args.word)


def test_lang_support(lang: str):
    if lang != 'all' and lang not in LANGUAGES:
        raise LanguageNotSupportedError(lang)
