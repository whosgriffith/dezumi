# Generated by Django 3.2.11 on 2022-03-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20220307_2038'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinteraction',
            name='posts_likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to='social.Post'),
        ),
    ]
