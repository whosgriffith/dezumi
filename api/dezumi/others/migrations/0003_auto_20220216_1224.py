# Generated by Django 3.2.11 on 2022-02-16 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('others', '0002_person_personmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('extra_fields', models.FileField(blank=True, null=True, upload_to='characters/extra_fields/')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_likes', models.IntegerField(default=0)),
                ('total_dislikes', models.IntegerField(default=0)),
                ('total_favorites', models.IntegerField(default=0)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='character_dislikes', to=settings.AUTH_USER_MODEL)),
                ('favorites', models.ManyToManyField(blank=True, related_name='character_favorites', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='character_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AlterModelOptions(
            name='personmedia',
            options={'verbose_name_plural': 'people media'},
        ),
        migrations.CreateModel(
            name='CharacterMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='people')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='others.character')),
            ],
            options={
                'verbose_name_plural': 'character media',
            },
        ),
    ]
