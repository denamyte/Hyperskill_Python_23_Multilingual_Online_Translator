import time
import requests
from bs4 import BeautifulSoup

from data import TranslationResult, TranslationResults, TranslationData
from exception import InternetConnectionError, CannotFindWordError

HEADERS = {'User-Agent': 'Mozilla/5.0'}


class ReversoQuery:
    def __init__(self, tr_data: TranslationData, limit: int):
        self._d = tr_data
        self._limit = limit
        self._trg_l = ''

    def _form_url(self) -> str:
        return f'https://context.reverso.net/translation/{self._d.src_l}-' \
               f'{self._trg_l}/{self._d.word}'

    def _make_query(self) -> requests.Response:
        url = self._form_url()
        for _ in range(5):
            r = requests.get(url, headers=HEADERS)
            if r.status_code == 404:
                raise CannotFindWordError(self._d.word)
            elif r:
                return r
            time.sleep(.02)
        raise InternetConnectionError()

    def _parse_response(self, resp: requests.Response) -> TranslationResult:
        soup = BeautifulSoup(resp.content, 'html.parser')
        words = [span.text.strip() for span in soup.find_all(
            'span', {'class': 'display-term'}, limit=self._limit)]
        examples = [div.text.strip() for div in soup.find_all(
            'div', {'class': ['src', 'trg']}, limit=self._limit * 4)]
        ex_tuples = list(zip(examples[::4], examples[1::4]))
        return TranslationResult(self._trg_l.capitalize(), words, ex_tuples)

    def _get_translation(self, trg_l) -> TranslationResult:
        self._trg_l = trg_l
        return self._parse_response(self._make_query())

    def get_translations(self) -> TranslationResults:
        return TranslationResults(
           [self._get_translation(trg_l) for trg_l in self._d.trg_ls]
        )


def make_queries(tr_data: TranslationData) -> TranslationResults:
    limit = 5 if len(tr_data.trg_ls) == 1 else 1
    return ReversoQuery(tr_data, limit).get_translations()
