from django.shortcuts import render
from dataset.models import DataSetJkh
# Create your views here.
# from src.dataset.models import DataSetJkh


def client_view(request, fio):
    objects = DataSetJkh.objects.filter(fio=fio)

    context = {'objects': objects,
               'fio': fio}
    return render(request, 'client.html', context)
