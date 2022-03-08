# Generated by Django 3.2.11 on 2022-03-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_initial'),
        ('shows', '0003_auto_20220303_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='characters',
            field=models.ManyToManyField(to='others.Character'),
        ),
        migrations.AlterField(
            model_name='show',
            name='people',
            field=models.ManyToManyField(through='shows.PersonShow', to='others.Person'),
        ),
    ]