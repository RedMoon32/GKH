import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from secrets import token
from core.models import UserData, VkSession
from src.bot.handlers import *
from src.gis.gislab import GisLab

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "183478400")

group_message_handlers = {
    "Загрузить файл": receive_file,
    "Список": get_list
}

user_message_handlers = {
    "Помощь": get_help,
    "Счетчики": get_data,
    "Сбросить": start,
    "ГИС": GisLab,
}

command_handlers = {
    UserStatuses.start: start,
    UserStatuses.enter_name: enter_name,
    UserStatuses.enter_role: enter_role,
    UserStatuses.enter_org_name: enter_org_name,
    UserStatuses.enter_user_org: enter_user_org_name,
    UserStatuses.approve: approve,
}


def process_message_from_user(event):
    if not UserData.objects.filter(vk_id=event.obj.from_id).exists():
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=TEST_DATA)
    user = UserData.objects.get_or_create(vk_id=event.obj.from_id)[0]
    user_session = VkSession.objects.get_or_create(user=user)[0]
    handler = command_handlers.get(user_session.status, None)
    print('STATUS:', user_session.status)
    if handler is None:
        if user.is_organisation:
            handler = group_message_handlers.get(event.obj.text, receive_file)
        else:
            handler = user_message_handlers.get(event.obj.text, get_help)
    res = handler(vk, event, user, user_session)
    print(res)
    if type(res) is str:
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=res)
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
