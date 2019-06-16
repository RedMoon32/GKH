from django.shortcuts import render

from core.models import UserData, Organisation
from dataset.models import DataSetJkh


# Create your views here.
# from src.dataset.models import DataSetJkh


def client_view(request, fio):
    objects = DataSetJkh.objects.filter(fio=fio)

    context = {'objects': objects,
               'fio': fio}
    return render(request, 'client.html', context)


def approved_list(request, company_id):
    users = []
    company = Organisation.objects.get(id=company_id)
    for name in DataSetJkh.objects.filter(organization=company.name).values('fio'):
        us = UserData.objects.filter(name=name['fio'])
        if us.exists():
            #    users.append(UserData(name=name['fio'], vk_id='-', approved='-'))
            # else:
            users.append(us[0])
        else:
            users.append(UserData(name=name['fio'], vk_id='-', approved='-'))

    context = {'company_name': company_id,
               'users': users}
    return render(request, 'company.html', context)
