from django.db import models


class Ant(models.Model):
    id = models.IntegerField(primary_key=True)
    ant_image = models.ImageField()
    chances = models.FloatField()


class Chest(models.Model):
    id = models.IntegerField(primary_key=True)
    chest_image = models.ImageField()
    chances = models.FloatField()
    cost = models.IntegerField()


class Boss(models.Model):
    id = models.IntegerField(primary_key=True)
    power = models.IntegerField()


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    chest = models.ForeignKey(Chest, on_delete=models.CASCADE)
    chest_open_time = models.DateTimeField(null=True)
    boss_date = models.DateField(null=True)


class UserAnts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    count = models.IntegerField(default=-1)
