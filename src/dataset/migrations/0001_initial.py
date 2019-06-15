# Generated by Django 2.2.2 on 2019-06-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetJkh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200, verbose_name='Дата')),
                ('object_adr', models.CharField(max_length=200, verbose_name='Объект')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО')),
                ('location', models.CharField(max_length=200, verbose_name='Место расположения')),
                ('field_1', models.CharField(max_length=200)),
                ('field_2', models.CharField(max_length=200)),
                ('field_3', models.CharField(max_length=200)),
                ('field_4', models.CharField(max_length=200)),
                ('field_5', models.CharField(max_length=200)),
                ('field_6', models.CharField(max_length=200)),
                ('field_7', models.CharField(max_length=200)),
                ('field_8', models.CharField(max_length=200)),
                ('field_9', models.CharField(max_length=200)),
                ('field_10', models.CharField(max_length=200)),
                ('field_11', models.CharField(max_length=200)),
                ('field_12', models.CharField(max_length=200)),
                ('field_13', models.CharField(max_length=200)),
                ('field_14', models.CharField(max_length=200)),
                ('field_15', models.CharField(max_length=200)),
                ('field_16', models.CharField(max_length=200)),
                ('field_17', models.CharField(max_length=200)),
                ('field_18', models.CharField(max_length=200)),
                ('field_19', models.CharField(max_length=200)),
                ('field_20', models.CharField(max_length=200)),
                ('field_21', models.CharField(max_length=200)),
                ('field_22', models.CharField(max_length=200)),
                ('organization', models.CharField(default='Cтриж', max_length=200)),
            ],
        ),
    ]
