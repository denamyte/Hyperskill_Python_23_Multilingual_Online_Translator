from dataclasses import  dataclass
from typing import List


@dataclass
class TranslationData:
    lang_from: str
    lang_to: str
    word: str


@dataclass
class TranslationResult:
    terms: List[str]
    sentences: List[str]
