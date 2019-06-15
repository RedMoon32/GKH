import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from secrets import token
from core.models import UserData, VkSession
from src.bot.handlers import *

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "183478400")

group_message_handlers = {
    "Загрузить файл": receive_file,

}

user_message_handlers = {
    "Помощь": get_help,
    "Счетчики": get_data,
    "Сбросить": downgrade,
}

command_handlers = {
    UserStatuses.start: start,
    UserStatuses.enter_address: enter_address,
    UserStatuses.enter_name: enter_name,
    UserStatuses.enter_role: enter_role,
    UserStatuses.enter_org_name: enter_org_name,
}


def process_message_from_user(event):
    user = UserData.objects.get_or_create(vk_id=event.obj.from_id)[0]
    user_session = VkSession.objects.get_or_create(user=user)[0]
    handler = command_handlers.get(user_session.status, None)
    if handler is None:
        if Organisation.objects.filter(vk_id=event.obj.from_id).exists():
            handler = group_message_handlers.get(event.obj.text, )
        else:
            handler = user_message_handlers.get(event.obj.text, get_help)
    handler(vk, event, user, user_session)
    user_session.save()
    user.save()


def start_bot():
    print("VK BOT IS WORKING")
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.obj.from_id, ' ', event.obj.text)
            if event.obj.text != '' and event.from_user:
                try:
                    process_message_from_user(event)
                except Exception as e:
                    print(str(e))
                    continue


if __name__ == "__main__":
    start_bot()
