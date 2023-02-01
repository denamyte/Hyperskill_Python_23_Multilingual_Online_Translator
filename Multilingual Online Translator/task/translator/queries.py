import requests
from bs4 import BeautifulSoup
from data import TranslationData, TranslationResult

REVERSO_LANGS = {'en': 'english',
                 'fr': 'french'}
HEADERS = {'User-Agent': 'Mozilla/5.0'}


class ReversoQueries:
    def __init__(self):
        self.resp: requests.Response | None = None

    @staticmethod
    def _form_url(tr_data: TranslationData) -> str:
        lfrom = REVERSO_LANGS.get(tr_data.lang_from)
        lto = REVERSO_LANGS.get(tr_data.lang_to)
        return f'https://context.reverso.net/translation/{lfrom}-{lto}/' \
               f'{tr_data.word}'

    def make_query(self, tr_data: TranslationData):
        url = self._form_url(tr_data)
        for _ in range(5):
            r = requests.get(url, headers=HEADERS)
            if r:
                self.resp = r
                break

    def parse_response(self):
        soup = BeautifulSoup(self.resp.content, 'html.parser')
        terms = [span.text.strip() for span in soup.find_all('span', {'class': 'display-term'})]
        sentences = [div.text.strip() for div in soup.find_all('div', {'class': ['src ltr', 'trg ltr']})]
        return TranslationResult(terms, sentences)
