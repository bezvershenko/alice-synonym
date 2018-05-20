from synonyms.config import SYNONYM_API
import requests
import  random


def get_synonym(text):
    try:
        request = requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?', params={
            'key': SYNONYM_API, 'lang': 'ru-ru', 'text': text
        }).json()['def'][0]['tr'][0]['syn']
        return 'Найден синоним: ' + requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?', params={
            'key': SYNONYM_API, 'lang': 'ru-ru', 'text': text
        }).json()['def'][0]['tr'][0]['syn'][random.randrange(len(request))]['text']
    except:
        return 'Синоним не найден'