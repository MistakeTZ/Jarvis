# Выход

from vacore import VACore

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Смена ражима", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "description": "Плагин\n"
                       "Голосовая команда: сменить режим",

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "режим|режима|сменить режим на|сменить режим": change_mode
        }
    }
    return manifest

def change_mode(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла
    if phrase == "пассивный":
        if core.mode == "passive":
            core.play_voice_assistant_speech("пассивный режим")
            return
        core.mode = "passive"
        core.play_voice_assistant_speech("режим изменен на пассивный")
    if "рабочий|работе|активный".find(phrase) != -1:
        if core.mode == "active":
            core.play_voice_assistant_speech("рабочий режим")
            return
        core.mode = "active"
        core.play_voice_assistant_speech("режим изменен на рабочий")
