from menus import Menus
from queries import ReversoQuery
from data import TranslationData


def main():
    menus = Menus()

    menus.welcome()
    tr_data = TranslationData(
        src_lang=menus.choose_first_lang(),
        trg_lang=menus.choose_second_lang(),
        word=menus.choose_word()
    )
    print(ReversoQuery().get_translation(tr_data))


if __name__ == '__main__':
    main()
