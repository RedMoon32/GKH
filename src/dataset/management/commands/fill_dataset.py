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
            print(item.values())
            rec = DataSetJkh(**item.values())
            rec.save()

