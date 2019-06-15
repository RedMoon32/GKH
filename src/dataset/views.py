from django.shortcuts import render

from core.models import UserData
from dataset.models import DataSetJkh


# Create your views here.
# from src.dataset.models import DataSetJkh


def client_view(request, fio):
    objects = DataSetJkh.objects.filter(fio=fio)

    context = {'objects': objects,
               'fio': fio}
    return render(request, 'client.html', context)


def approved_list(request, company_name):
    users = []
    for name in DataSetJkh.objects.all().values('fio'):
        us = UserData.objects.filter(name=name)
        if not us.exists():
            users.append(UserData(name=name['fio'], vk_id='-', approved='-'))
        else:
            users.append(us[0])
    context = {'company_name': company_name,
               'users': users}
    return render(request, 'company.html', context)
