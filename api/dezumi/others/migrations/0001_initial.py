# Generated by Django 3.2.11 on 2022-02-28 17:18

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('extra_info', models.FileField(blank=True, null=True, upload_to='characters/extra_fields/')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_likes', models.PositiveBigIntegerField(default=0)),
                ('total_dislikes', models.PositiveBigIntegerField(default=0)),
                ('total_favorites', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6, null=True)),
                ('total_likes', models.PositiveBigIntegerField(default=0)),
                ('total_followers', models.PositiveBigIntegerField(default=0)),
                ('total_favorites', models.PositiveBigIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='PersonVisual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='people/visual/')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visual', to='others.person')),
            ],
            options={
                'verbose_name_plural': 'people visuals',
            },
        ),
        migrations.CreateModel(
            name='CharacterVisual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='characters/visual/')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visual', to='others.character')),
            ],
            options={
                'verbose_name_plural': 'character visuals',
            },
        ),
    ]
