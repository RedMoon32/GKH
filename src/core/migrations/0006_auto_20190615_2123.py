# Generated by Django 2.2.2 on 2019-06-15 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190615_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='files',
        ),
        migrations.DeleteModel(
            name='CSV_File',
        ),
    ]
