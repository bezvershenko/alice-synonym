from synonyms.config import SYNONYM_API
import requests


def get_synonym(text):
    try:
        return 'Найден синоним: ' + requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?', params={
            'key': SYNONYM_API, 'lang': 'ru-ru', 'text': text
        }).json()['def'][0]['tr'][0]['syn'][0]['text']
    except:
        return 'Синонимы не найдены'
