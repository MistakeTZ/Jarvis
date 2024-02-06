# Рандом

from vacore import VACore
from utils.num_to_text_ru import num2text


# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Калькулятор", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "description": "Демонстрационный плагин\n"
                       "Голосовая команда: счет, сколько",

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "плюс|минус|умножь|умножить|поделить|подели|на|равно|равен": count
        }
    }
    return manifest

def play_coin(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
                                              # если юзер сказал больше
                                              # в этом плагине не используется
    arrR = [
        "Выпал орел",
        "Выпала решка",
    ]
    core.play_voice_assistant_speech(arrR[random.randint(0, len(arrR) - 1)])

def play_dice(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
    # если юзер сказал больше
    # в этом плагине не используется
    arrR = [
        "Выпала единица",
        "Выпало два",
        "Выпало три",
        "Выпало четыре",
        "Выпало пять",
        "Выпало шесть",
    ]
    core.play_voice_assistant_speech(arrR[random.randint(0, len(arrR) - 1)])

def count(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла

    res = 0.0
    core.play_voice_assistant_speech(num2text(res))