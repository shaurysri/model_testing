import nltk
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def fetch_abusive_text(text, abuse_words):
    abuse_text = []
    for word in nltk.word_tokenize(text.lower()):
        for tw in abuse_words:
            if word in tw:
                abuse_text.append(word)

    abuse_text = ' '.join(list(set(abuse_text)))
    return abuse_text


def is_abusive(text, abuse_text):
    is_abusive_text = False
    abuse_percent = similar(text, abuse_text)
    if abuse_percent >= 0.20:
        is_abusive_text = True
    return is_abusive_text


def get_abusive_scores(is_abusive_text):
    lexical_score = 0
    type_score = 0
    if is_abusive_text:
        lexical_score += 5
        type_score += 1

    return lexical_score, type_score
