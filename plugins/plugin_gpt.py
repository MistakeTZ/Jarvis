# GPT

import random
import requests
import os
from vacore import VACore

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "GPT", # имя
        "version": "1.0", # версия
        "require_online": True, # требует ли онлайн?

        "description": "Демонстрационный плагин\n"
                       "Голосовая команда: сколько будет",

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "что такое": what_is,
            "ответь|скажи": ans
        }
    }
    return manifest

def ans(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
    answer = send_request("Ты - ассистент Джарвис. Просто коротко ответь на вопрос", phrase)
    if answer:
        core.play_voice_assistant_speech(answer)


def what_is(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
    if phrase:
        answer = send_request("Ответь очень коротко что это такое", phrase)
        if answer:
            core.play_voice_assistant_speech(answer)


def send_request(system, answer, assistant=None, temperature=0.3, max_tokens="300", *args):
    
    prompt = {
        "modelUri": "gpt://b1g32u6e1hl8eg5pj2os/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": temperature,
            "maxTokens": max_tokens
        },
        "messages": [
            {
                "role": "system",
                "text": system
            },
            {
                "role": "user",
                "text": answer
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key " + os.getenv("gpt_key")
    }

    response = requests.post(url, headers=headers, json=prompt)
    result =  response.json()
    if "result" in result:
        if "alternatives" in result["result"]:
            if "message" in result["result"]["alternatives"][0]:
                return result["result"]["alternatives"][0]["message"]["text"]
    return False


