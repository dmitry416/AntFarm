from django.db import models

class Ant(models.Model):
    pass

class Chest(models.Model):
    pass

class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=32)
    chest = models.OneToOneField(Chest, on_delete=models.CASCADE)
    chest_open_time = models.DateTimeField(null=True)
    boss_date = models.DateField(null=True)

class UserAnts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    count = models.IntegerField(default=-1)


