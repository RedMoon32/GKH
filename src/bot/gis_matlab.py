import matlab.engine

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from secrets import token

def gisML(vk_chat):
    eng = matlab.engine.start_matlab()
    sA=eng.workspace["sol"]
    vk_chat.messages.send(user_id=event.obj.from_id,
                          random_id=get_random_id(),
                          message="Matlab here")
    eng.quit()

def start_chat():
    vk_session = vk_api.VkApi(token=token)
    # пример  vk_session = vk_api.VkApi(token = "a6f87v8c9a9sa87a7af9a0f9f9v8a6s6c5b5m6n8bds09asc8d7b87d87bd87n"
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, "183478400")
    # пример longpoll = VkBotLongPoll(vk_session, "637182735")
    for event in longpoll.listen():  # Проверка действий
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.type == VkBotEventType.MESSAGE_NEW:  # последняя строчка
                # проверяем не пустое ли сообщение нам пришло
                if event.obj.text != '':
                    # проверяем пришло сообщение от пользователя или нет
                    if event.from_user:
                        gisML(vk)


if __name__=="__main__":
    start_chat()
