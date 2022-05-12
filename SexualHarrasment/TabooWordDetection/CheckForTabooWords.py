import json
import nltk
import pandas as pd


def read_json_file(filename):
    data = []
    json_data = open(filename).read()
    if json_data == "":
        return data
    else:
        data = json.loads(json_data)
    return data


def get_grammar(text):
    return ' '.join([t for w, t in nltk.pos_tag(nltk.word_tokenize(text))])


def create_df(data):
    df = pd.DataFrame()
    if data:
        df = pd.DataFrame(
            [{'taboo_cat': ty, 'type': w, 'text': i} for ty, c in data[0].items() for w, t in c.items() for i in t])
        df['nlp'] = df['text'].apply(get_grammar)
    return df


def get_possible_nlp(df):
    return set(
        list(df['nlp'][df['type'] == 'words'].unique()) + list(df['nlp'][df['type'] == 'phrases'].unique())), list(
        df['text'])


def check_taboo_pos(text_pos, taboo_pos):
    is_taboo_pos = False
    if text_pos in taboo_pos:
        is_taboo_pos = True
    return is_taboo_pos


def check_taboo_text(text, taboo_words):
    taboo_text = False
    for words in nltk.word_tokenize(text.lower()):
        for tw in taboo_words:
            if words in tw:
                taboo_text = True
    return taboo_text


def check_taboowords(text, taboo_words_pos, taboo_words):
    is_taboo_text = False
    is_taboo_pos = False
    text_pos = check_text_pos(text)
    if check_taboo_pos(text_pos, taboo_words_pos):
        is_taboo_pos = True
    if check_taboo_text(text, taboo_words):
        is_taboo_text = True
    return is_taboo_text, is_taboo_pos


def check_text_pos(text):
    word_tokens = nltk.word_tokenize(text.lower())
    text_pos = [tag for words, tag in nltk.pos_tag(word_tokens)]
    return ' '.join(text_pos)


def get_taboo_scores(is_taboo_text, is_taboo_pos):
    lexical_score = 0
    type_score = 0

    if is_taboo_pos:
        lexical_score += 10
        type_score += 1

    if is_taboo_text:
        lexical_score += 10
        type_score += 1
    return lexical_score, type_score
