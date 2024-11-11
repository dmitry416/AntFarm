from django.db import models


class Item(models.Model):
    path_to_image = models.CharField(max_length=255)
    middle_cost = models.IntegerField(default=1)
    cost = models.IntegerField(default=1)


class Ant(models.Model):
    path_to_image = models.CharField(max_length=255)
    minimal_cost = models.IntegerField()


class AntItemChance(models.Model):
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    weight = models.IntegerField()


class Chest(models.Model):
    path_to_image = models.CharField(max_length=255)
    cost = models.IntegerField()


class ChestAntChance(models.Model):
    chest = models.ForeignKey(Chest, on_delete=models.CASCADE)
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    weight = models.IntegerField()


class Boss(models.Model):
    path_to_image = models.CharField(max_length=255)
    power = models.IntegerField()


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=32)
    image_url = models.CharField(max_length=255, null=True)

    chest = models.ForeignKey(Chest, on_delete=models.SET_NULL, null=True)
    chest_open_time = models.DateTimeField(null=True)

    ant_count = models.IntegerField(default=0)

    money = models.IntegerField(default=0)
    boss_date = models.DateField(null=True)


class UserAnts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    count = models.IntegerField(default=-1)
    is_sent = models.BooleanField(default=False)
    return_datetime = models.DateTimeField(null=True)


class UserItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField()


class ServerState(models.Model):
    current_boss = models.ForeignKey(Boss, on_delete=models.SET_NULL, null=True)
    boss_update_time = models.DateTimeField(null=True)
