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
    text = analyze(word_to_search)
    if text is None:
        response.set_text('Я тебя не поняла. Назови слово, синоним к которому ты хочешь подобрать.')
    else:
        response.set_text(get_synonym(text))
    return response, user_storage


def analyze(response):
    whitelist = ['найти', 'придумать', 'сказать', 'подсказать']
    text = re.findall('([а-яА-Я\-]+)', response)

    if len(text) == 1:
        return text
    else:
        parser = MorphAnalyzer()
        a = []
        for word in text:
            a.append((word, parser.parse(word)[0]))
        if {'VERB', 'INFN'} & a[0][1].tag.grammemes:
            verb = a.pop(0)
            if verb[1].normal_form not in whitelist:
                return None

        # print(a[0][0])
        if a[0][0] == 'синоним':
            if a[1][0] in ('к', 'для'):
                if a[2][1].normal_form == 'слово':
                    return a[3][0]
            if a[1][1].normal_form == 'слово':
                return a[2][0]

        return None


print(analyze('синоним слову красивый'))
