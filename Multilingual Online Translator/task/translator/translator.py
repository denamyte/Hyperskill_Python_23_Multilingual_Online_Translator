from menus import Menus
from queries import ReversoQueries


def main():
    menus = Menus()
    queries = ReversoQueries()

    menus.choose_lang()
    menus.choose_word()
    menus.confirm_chosen()

    queries.make_query(menus.data)
    menus.confirm_query()
    res = queries.parse_response()
    print(res)


if __name__ == '__main__':
    main()
