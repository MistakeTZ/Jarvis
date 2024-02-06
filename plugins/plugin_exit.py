# Выход

import random
from vacore import VACore

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Выход", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "description": "Плагин\n"
                       "Голосовая команда: выход, стоп",

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "стоп|выход|останови программу": stop
        }
    }
    return manifest

def stop(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла
    exit()
