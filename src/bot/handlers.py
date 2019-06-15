# Todo вынести переменную сессию бота в отдельный файл
from vk_api.utils import get_random_id

from core.models import UserStatuses, Organisation, CSV_File
from src.bot.messages import *
import urllib.request
import os
from GKH.settings import *


def start(vk, event, user, session):
    for mess in [WELCOME, IS_ORGANISATION]:
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=mess)
    session.status = UserStatuses.enter_role


def enter_role(vk, event, user, session):
    if event.obj.text.lower() == "да":
        org = Organisation.objects.get_or_create(vk_id=event.obj.from_id)[0]
        org.save()
        session.status = UserStatuses.enter_org_name
        user.organisation = True
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=ORGANISATION_NAME)
    else:
        session.status = UserStatuses.enter_name
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=ENTER_NAME)


def enter_org_name(vk, event, user, session):
    org = Organisation.objects.get_or_create(vk_id=event.obj.from_id)[0]
    org.name = event.obj.text
    org.save()
    session.status = UserStatuses.allowed_group
    vk.messages.send(
        user_id=event.obj.from_id,
        random_id=get_random_id(),
        message=FILES)


def receive_file(vk, event, user, session):
    if len(event.obj.attachments) == 0:
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message='Пожалуйста приложите файл к сообщению')
    else:
        new = CSV_File.objects.create()
        org = Organisation.objects.get(vk_id=event.obj.from_id)
        new.file_path = os.path.join(BASE_DIR, "files") + f"/{new.id}.csv"
        open(new.file_path, "w")
        urllib.request.urlretrieve(event.obj.attachments[0]["doc"]["url"], new.file_path)
        org.files.add(new)
        org.save()
        new.save()
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message='Показания счетчиков загружены для просмотра пользователей')


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
