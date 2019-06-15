import csv
import os, json
from random import random

from django.core.management.base import BaseCommand

from dataset.models import DataSetJkh

JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def load_from_csv(file_name):
    # with open(os.path.join(JSON_PATH, file_name + '.csv'), 'r') as infile:
    #     return json.load(infile)
    csv_rows = []
    with open(os.path.join(JSON_PATH, file_name + '.csv'), 'r') as csvfile:
        # reader = csv.reader(csvfile, delimiter=';')
        reader = csv.DictReader(csvfile, delimiter=';')
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
    return csv_rows


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = load_from_csv('water')
        for item in data:
            i = {}
            print(item)
            i['data'] = item['Дата']
            i['object_adr'] = item['Объект']
            i['fio'] = item['ФИО']
            i['location'] = item['Место расположения']
            i['field_1'] = item['ХВС модель ПУ']
            i['field_2'] = item['ХВС сер. ном.']
            i['field_3'] = item['ХВС ID']
            i['field_4'] = item['ХВС нач., м3']
            i['field_5'] = item['ХВС кон., м3']
            i['field_6'] = item['ХВС потр., м3']
            i['field_7'] = item['Последнее сообщение']
            i['field_8'] = item['Внимание']
            i['field_9'] = item['Примечания']
            print(i)

            rec = DataSetJkh(**i)
            rec.save()
