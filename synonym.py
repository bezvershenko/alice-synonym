# coding: utf-8
from __future__ import unicode_literals
from synonyms import get_synonym
from pymorphy2 import MorphAnalyzer
import re


# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    if request.is_new_session:
        response.set_text('Привет! Назови слово, к которому нужно подобрать синоним.')
        return response, user_storage
    word_to_search = request.command.lower()
    response.set_text(get_synonym(word_to_search))
    return response, user_storage


def analyze(response):
    text = re.findall('([а-яА-Я\-]+)', response)
    print(text)

    l = len(text)
    if l == 1:
        return text
    else:
        parser = MorphAnalyzer()
        a = []
        for word in text:
            a.append((word, parser.parse(word)[0]))
        if {'VERB', 'INFN'}&a[0][1].tag.grammemes and a[1][0] == 'синоним':
            if a[2][0] in ('к', 'для'):
                if a[3][0].startswith('слово'):
                    pass
analyze('прив-ет, алиса')

