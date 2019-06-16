import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from secrets import token
from core.models import UserData, VkSession

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "183478400")
