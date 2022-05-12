import ast

import nltk


def read_txt_list(file_path):
    data = []
    try:
        text_file = open(file_path, "r")
        lines = text_file.readline()
        data = ast.literal_eval(lines)
    except Exception as e:
        print(e)
    return data


def check_text_pos(text):
    word_tokens = nltk.word_tokenize(text.lower())
    text_pos = [tag for words, tag in nltk.pos_tag(word_tokens)]
    return ' '.join(text_pos)


def is_swear_pos(text_pos, swear_words_pos):
    swear_pos = False
    if text_pos in swear_words_pos:
        swear_pos = True
    return swear_pos


def is_swear_text(text, swear_words):
    swear_text = False
    for words in nltk.word_tokenize(text.lower()):
        for sw in swear_words:
            if words in sw:
                swear_text = True
    return swear_text


def check_swearing(text, swear_words_pos, swear_words):
    is_swearing_text = False
    is_swearing_pos = False
    text_pos = check_text_pos(text)
    if is_swear_pos(text_pos, swear_words_pos):
        is_swearing_pos = True
    if is_swear_text(text, swear_words):
        is_swearing_text = True
    return is_swearing_text, is_swearing_pos


def get_swear_scores(is_swearing_text, is_swearing_pos):
    lexical_score = 0
    type_score = 0

    if is_swearing_pos:
        lexical_score += 1
        type_score += 1

    if is_swearing_text:
        lexical_score += 1
        type_score += 1

    return lexical_score, type_score
