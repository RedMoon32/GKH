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

