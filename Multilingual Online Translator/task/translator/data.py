from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TranslationData:
    src_l: str
    trg_l: List[str]
    word: str


@dataclass
class TranslationResult:
    target_lang: str
    words: List[str]
    examples: List[Tuple[str, str]]

    def __str__(self):
        words = '\n'.join(w for w in self.words)
        examples = '\n\n'.join(f'{s1}\n{s2}' for s1, s2 in self.examples)
        return f"""\
{self.target_lang} Translations:
{words}

{self.target_lang} Examples:
{examples}"""


@dataclass
class TranslationResults:
    results: List[TranslationResult]

    def __str__(self):
        return '\n\n\n'.join(str(res) for res in self.results or [])
