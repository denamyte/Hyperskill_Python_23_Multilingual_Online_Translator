import requests
from bs4 import BeautifulSoup
from data import TranslationData, TranslationResult

REVERSO_LANGS = {'en': 'english',
                 'fr': 'french'}
HEADERS = {'User-Agent': 'Mozilla/5.0'}


class ReversoQueries:
    def __init__(self):
        self.resp: requests.Response | None = None
        self._trg_lang = ''

    def _form_url(self, tr_data: TranslationData) -> str:
        src_lang = REVERSO_LANGS.get(tr_data.lang_from)
        self._trg_lang = REVERSO_LANGS.get(tr_data.lang_to)
        return f'https://context.reverso.net/translation/{src_lang}-' \
               f'{self._trg_lang}/{tr_data.word}'

    def make_query(self, tr_data: TranslationData):
        url = self._form_url(tr_data)
        for _ in range(5):
            r = requests.get(url, headers=HEADERS)
            if r:
                self.resp = r
                break

    def parse_response(self):
        soup = BeautifulSoup(self.resp.content, 'html.parser')
        words = [span.text.strip() for span in soup.find_all('span', {'class': 'display-term'})]
        examples = [div.text.strip() for div in soup.find_all('div', {'class': ['src ltr', 'trg ltr']})]
        ex_tuples = list(zip(examples[::2], examples[1::2]))
        return TranslationResult(self._trg_lang.capitalize(), words, ex_tuples)
