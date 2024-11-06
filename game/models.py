from django.db import models
from django.template.defaultfilters import default


class Ant(models.Model):
    path_to_image = models.CharField(max_length=255)
    chances = models.FloatField(default)


class Chest(models.Model):
    path_to_image = models.CharField(max_length=255)
    chances = models.FloatField()
    cost = models.IntegerField()


class Boss(models.Model):
    path_to_image = models.CharField(max_length=255)
    power = models.IntegerField()


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=32)
    image_url = models.CharField(max_length=255, null=True)

    chest = models.ForeignKey(Chest, on_delete=models.CASCADE)
    chest_open_time = models.DateTimeField(null=True)

    ant_count = models.IntegerField(default=0)

    money = models.IntegerField(default=0)
    boss_date = models.DateField(null=True)


class UserAnts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    count = models.IntegerField(default=-1)
