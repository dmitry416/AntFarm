# Generated by Django 5.1.2 on 2024-10-31 13:18

import django.db.models.deletion
import django.template.defaultfilters
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_image', models.CharField(max_length=255)),
                ('chances', models.FloatField(verbose_name=django.template.defaultfilters.default)),
            ],
        ),
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_image', models.CharField(max_length=255)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_image', models.CharField(max_length=255)),
                ('chances', models.FloatField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=32)),
                ('chest_open_time', models.DateTimeField(null=True)),
                ('boss_date', models.DateField(null=True)),
                ('chest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.chest')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=-1)),
                ('ant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.ant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.user')),
            ],
        ),
    ]