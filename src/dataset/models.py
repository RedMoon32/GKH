import csv
import os

from django.db import models


# Create your models here.

class DataSetJkh(models.Model):
    # 00 = {str} 'Дата'
    data = models.CharField('Дата', max_length=200)
    # 01 = {str} 'Объект'
    object_adr = models.CharField('Объект', max_length=200)
    # 02 = {str} 'ФИО'
    fio = models.CharField('ФИО', max_length=200)
    # 03 = {str} 'Место расположения'
    location = models.CharField('Место расположения', max_length=200)
    # 04 = {str} 'ХВС модель ПУ'
    field_1 = models.CharField(max_length=200)
    # 05 = {str} 'ХВС сер. ном.'
    field_2 = models.CharField(max_length=200)
    # 06 = {str} 'ХВС ID'
    field_3 = models.CharField(max_length=200)
    # 07 = {str} 'ХВС нач., м3'
    field_4 = models.CharField(max_length=200)
    # 08 = {str} 'ХВС кон., м3'
    field_5 = models.CharField(max_length=200)
    # 09 = {str} 'ХВС потр., м3'
    field_6 = models.CharField(max_length=200)
    # 10 = {str} 'Последнее сообщение'
    field_7 = models.CharField(max_length=200)
    # 11 = {str} 'Внимание'
    field_8 = models.CharField(max_length=200)
    # 12 = {str} 'Примечания'
    field_9 = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, default='Cтриж')
    paid = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)


def import_data_from_csv(file_name, organization_name=''):
    def load_from_csv(file_name):
        csv_rows = []
        with open(file_name, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            title = reader.fieldnames
            for row in reader:
                csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
        return csv_rows

    data = load_from_csv(file_name)
    refield = {'Дата': 'data',
               'Объект': 'object_adr',
               'ФИО': 'fio',
               'Место расположения': 'location',
               'ХВС модель ПУ': 'field_1',
               'ХВС сер. ном.': 'field_2',
               'ХВС ID': 'field_3',
               'ХВС нач., м3': 'field_4',
               'ХВС кон., м3': 'field_5',
               'ХВС потр., м3': 'field_6',
               'Последнее сообщение': 'field_7',
               'Внимание': 'field_8',
               'Примечания': 'field_9',
               }
    for item in data:
        rec = DataSetJkh(**{refield[key]: item[key] for key in refield.keys()})
        rec.save()
    return True


# import_data_from_csv('C:\work\хакартон\GKH\src\dataset\management\commands\data\water.csv')

def set_default_names():
    i = 1
    for item in DataSetJkh.objects.all():
        item.fio = f'Имя{round(i)}'
        item.save()
        i += 0.5


# set_default_names()


def get_bill_by_name(name):
    result = ''
    for item in DataSetJkh.objects.filter(fio=name):
        result += f'ФИО {item.fio} ; Объект {item.object_adr} ; ID счётчик {item.field_2} ; ХВС потр., м3 {item.field_6} \n '
    return result

# print(get_bill_by_name('Имя2'))
