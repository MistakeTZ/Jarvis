# Калькулятор

from vacore import VACore
from Calculator.main import calculator

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Калькулятор", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "description": "Плагин\n"
                       "Голосовая команда: сколько будет",

        "commands": {
            "сколько будет|посчитай|сколько|почитай|пример": calculate
        }
    }
    return manifest

def calculate(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
                                              # если юзер сказал больше
                                              # в этом плагине не используется
    calculator(core, phrase)
