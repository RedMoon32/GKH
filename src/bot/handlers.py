# Todo вынести переменную сессию бота в отдельный файл
import threading

from vk_api.utils import get_random_id

from core.models import UserStatuses, Organisation, UserData
from dataset.models import import_data_from_csv, get_bill_by_name, DataSetJkh
from src.bot.messages import *
import urllib.request
import os
from GKH.settings import *

temp_file_lock = 0


def get_list(vk, event, user, session):
    users = []
    company = Organisation.objects.get(vk_id=user.vk_id)
    MESS = "Список пользователей не подтвердивших расчеты с приборов учета контроля: "
    approved = []
    declined = []
    awaiting = []
    for info in DataSetJkh.objects.filter(organization=company.name):
        us = UserData.objects.filter(name=info.fio)
        if us.exists():
            us = us[0]
            if us.approved:
                approved.append(us)
            elif us.approved is False:
                declined.append(us)
            else:
                awaiting.append(us)
    if len(declined) > 0:
        for appr in declined:
            MESS += str(appr)
    return MESS


def start(vk, event, user, session):
    for mess in [WELCOME, IS_ORGANISATION]:
        vk.messages.send(
            user_id=event.obj.from_id,
            random_id=get_random_id(),
            message=mess)
    session.status = UserStatuses.enter_role


def enter_role(vk, event, user, session):
    if event.obj.text.lower() == YES:
        org = Organisation.objects.get_or_create(vk_id=event.obj.from_id)[0]
        org.save()
        session.status = UserStatuses.enter_org_name
        user.is_organisation = True
        return ORGANISATION_NAME
    else:
        session.status = UserStatuses.enter_name
        return ENTER_NAME


def enter_user_org_name(vk, event, user, session):
    org = Organisation.objects.filter(name=event.obj.text)
    if not org.exists():
        return NO_SUCH_ORG
    else:
        user.organisation = org[0]
        session.status = UserStatuses.allowed
        return CAN_GET_INFO


def get_approved(vk, event, user, session):
    return f"client/company/{user}/"


def enter_org_name(vk, event, user, session):
    org = Organisation.objects.get_or_create(vk_id=event.obj.from_id)[0]
    org.name = event.obj.text
    org.save()
    session.status = UserStatuses.allowed_group
    return CAN_UPLOAD_FILES


def receive_file(vk, event, user, session):
    if len(event.obj.attachments) == 0:
        return ATTACH_FILE
    else:
        global temp_file_lock
        temp_file_lock += 1
        org = Organisation.objects.get(vk_id=event.obj.from_id)
        file_path = os.path.join(BASE_DIR, "files") + f"/{temp_file_lock}.csv"
        open(file_path, "w")
        urllib.request.urlretrieve(event.obj.attachments[0]["doc"]["url"], file_path)
        # threading.Thread(target=process_file, args=(file_path, org))
        for user in UserData.objects.filter(organisation=org):
            user.approved = None
            user.save()
        import_data_from_csv(file_path, org.name)
        org.save()
        return LOADED


# def enter_address(vk, event, user, session):
#     user.address = event.obj.text
#     session.status = UserStatuses.enter_user_org
#     return ENTER_ORG_NAME


def get_help(vk, event, user, session):
    return AVAILABLE_COMMANDS


def get_data(vk, event, user, session):
    session.status = UserStatuses.approve
    if user.approved is None:
        return INFO + get_bill_by_name(user.name) + "\n" + APPROVED
    else:
        return INFO + get_bill_by_name(user.name)


def approve(vk, event, user, session):
    mess = event.obj.text.lower()
    if not (mess != YES or mess != NO):
        return ERROR
    if mess == YES:
        user.approved = True
    elif mess == NO:
        user.approved = False
    session.status = UserStatuses.allowed
    return THANKS + "\n" + AVAILABLE_COMMANDS


def enter_name(vk, event, user, session):
    user.name = event.obj.text
    session.status = UserStatuses.enter_user_org
    return ENTER_ORG_NAME
