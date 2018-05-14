# coding: utf-8
from __future__ import unicode_literals
from synonyms import get_synonym


# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    if request.is_new_session:
        response.set_text('Привет! Назови слово, к которому нужно подобрать синоним.')
        return response, user_storage
    word_to_search = request.command.lower()
    response.set_text(get_synonym(word_to_search))
    return response, user_storage
