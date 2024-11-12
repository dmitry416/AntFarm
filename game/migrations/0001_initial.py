# Generated by Django 5.1.2 on 2024-11-11 15:35

import django.db.models.deletion
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
                ('minimal_cost', models.IntegerField()),
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
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_image', models.CharField(max_length=255)),
                ('middle_cost', models.IntegerField(default=1)),
                ('cost', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ChestAntChance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('ant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.ant')),
                ('chest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.chest')),
            ],
        ),
        migrations.CreateModel(
            name='AntItemChance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('ant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.ant')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.item')),
            ],
        ),
        migrations.CreateModel(
            name='ServerState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss_update_time', models.DateTimeField(null=True)),
                ('current_boss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.boss')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32)),
                ('image_url', models.CharField(max_length=255, null=True)),
                ('chest_open_time', models.DateTimeField(null=True)),
                ('ant_count', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
                ('boss_date', models.DateField(null=True)),
                ('chest', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.chest')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=-1)),
                ('is_sent', models.BooleanField(default=False)),
                ('return_datetime', models.DateTimeField(null=True)),
                ('ant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.ant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.user')),
            ],
        ),
    ]
