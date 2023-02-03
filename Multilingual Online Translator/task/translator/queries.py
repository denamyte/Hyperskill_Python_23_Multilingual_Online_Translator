import time
from typing import List
import requests
from bs4 import BeautifulSoup

from data import TranslationResult, TranslationResults, TranslationData

HEADERS = {'User-Agent': 'Mozilla/5.0'}


class ReversoQuery:
    def __init__(self, src_l: str, trg_l: str, word: str, limit: int):
        self._src_l = src_l
        self._trg_l = trg_l
        self._word = word
        self._limit = limit

    def _form_url(self) -> str:
        return f'https://context.reverso.net/translation/{self._src_l}-' \
               f'{self._trg_l}/{self._word}'

    def _make_query(self) -> requests.Response:
        url = self._form_url()
        for _ in range(5):
            r = requests.get(url, headers=HEADERS)
            if r:
                return r
            time.sleep(.02)

    def _parse_response(self, resp: requests.Response) -> TranslationResult:
        soup = BeautifulSoup(resp.content, 'html.parser')
        words = [span.text.strip() for span in soup.find_all(
            'span', {'class': 'display-term'}, limit=self._limit)]
        examples = [div.text.strip() for div in soup.find_all(
            'div', {'class': ['src', 'trg']}, limit=self._limit * 4)]
        ex_tuples = list(zip(examples[::4], examples[1::4]))
        return TranslationResult(self._trg_l.capitalize(), words, ex_tuples)

    def get_translation(self) -> TranslationResult:
        resp = self._make_query()
        return self._parse_response(resp)


def make_queries(tr_data: TranslationData):
    limit = 5 if len(tr_data.trg_l) == 1 else 1
    return TranslationResults(
        [ReversoQuery(tr_data.src_l, tr_data.trg_l[i], tr_data.word, limit).
         get_translation() for i in range(len(tr_data.trg_l))]
    )
