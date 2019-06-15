# Todo вынести переменную сессию бота в отдельный файл
from vk_api.utils import get_random_id

from core.models import UserStatuses
from src.bot.messages import *


def start(vk, event, user, session):
    for mess in [WELCOME, ENTER_NAME]:
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=mess)
    session.status = UserStatuses.enter_name


def enter_address(vk, event, user, session):
    user.address = event.obj.text
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=CAN_GET_INFO)
    session.status = UserStatuses.allowed


def get_help(vk, event, user, session):
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=AVAILABLE_COMMANDS)


def downgrade(vk, event, user, session):
    session.status = UserStatuses.start
    start(vk, event, user, session)


def get_data(vk, event, user, session):
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=INFO)


def enter_name(vk, event, user, session):
    user.name = event.obj.text
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=ENTER_ADDRESS)
    session.status = UserStatuses.enter_address


def send__message():
    pass
