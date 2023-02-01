import time
import requests
from bs4 import BeautifulSoup
from data import TranslationData, TranslationResult

HEADERS = {'User-Agent': 'Mozilla/5.0'}


class ReversoQuery:
    @staticmethod
    def _form_url(tr_data: TranslationData) -> str:
        return f'https://context.reverso.net/translation/{tr_data.src_lang}-' \
               f'{tr_data.trg_lang}/{tr_data.word}'

    @staticmethod
    def _make_query(tr_data: TranslationData) -> requests.Response:
        url = ReversoQuery._form_url(tr_data)
        for _ in range(5):
            r = requests.get(url, headers=HEADERS)
            if r:
                return r
            time.sleep(.02)

    @staticmethod
    def _parse_response(resp: requests.Response, trg_lang: str) -> TranslationResult:
        soup = BeautifulSoup(resp.content, 'html.parser')
        words = [span.text.strip() for span in soup.find_all('span', {'class': 'display-term'})]
        examples = [div.text.strip() for div in soup.find_all('div', {'class': ['src ltr', 'trg ltr']})]
        ex_tuples = list(zip(examples[::2], examples[1::2]))
        return TranslationResult(trg_lang.capitalize(), words, ex_tuples)

    @staticmethod
    def get_translation(tr_data: TranslationData) -> TranslationResult:
        resp = ReversoQuery._make_query(tr_data)
        return ReversoQuery._parse_response(resp, tr_data.trg_lang)
