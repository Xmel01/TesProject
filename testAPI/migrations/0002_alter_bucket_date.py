# Generated by Django 4.1.2 on 2022-10-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата добавления'),
        ),
    ]
