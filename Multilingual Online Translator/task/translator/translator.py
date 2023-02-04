from arguments import parse_args
from queries import make_queries


def main():
    try:
        tr_data = parse_args()
        results = make_queries(tr_data)

        res_str = str(results)
        with open(f'{tr_data.word}.txt', 'w') as f:
            f.write(res_str)
        print(res_str)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
