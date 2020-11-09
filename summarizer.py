from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import constants

LANGUAGE = "english"


def get_summary(text: str, sentence_count: int) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = ""
    for sentence in summarizer(parser.document, sentence_count):
        summary += (str(sentence) + ". ")
    return summary


if __name__ == "__main__":
    get_summary(constants.test_text)
