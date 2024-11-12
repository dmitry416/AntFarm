import random

from django.db import models


class Item(models.Model):
    path_to_image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    middle_cost = models.IntegerField(default=1)
    cost = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Ant(models.Model):
    path_to_image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    minimal_cost = models.IntegerField()
    expedition_duration = models.DurationField()

    def get_random_item(self):
        ant_item_chances = AntItemChance.objects.filter(ant=self)
        print(ant_item_chances)
        weights = [chance.weight for chance in ant_item_chances]
        ant_item_chance = random.choices(ant_item_chances, weights=weights, k=1)[0]
        print(ant_item_chance)
        return ant_item_chance.item

    def __str__(self):
        return self.name


class AntItemChance(models.Model):
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.ant.name}->{self.item.name}'


class Chest(models.Model):
    path_to_image = models.CharField(max_length=255)
    cost = models.IntegerField()
    weight = models.IntegerField()


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

    chest = models.ForeignKey(Chest, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    chest_open_time = models.DateTimeField(null=True, blank=True)

    ant_count = models.IntegerField(default=0)

    money = models.IntegerField(default=0)
    boss_date = models.DateField(null=True, blank=True)


class UserAnts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ant = models.ForeignKey(Ant, on_delete=models.CASCADE)
    count = models.IntegerField(default=-1)
    is_sent = models.BooleanField(default=False)
    return_datetime = models.DateTimeField(null=True, blank=True, default=None)

    def get_cost(self):
        if self.count == 0:
            return 0

        return int((1.2 * self.ant.minimal_cost) ** self.count)

    def __str__(self):
        return f'{self.user.name}->{self.ant.name}'


class UserItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.name}->{self.item.name}'

class ServerState(models.Model):
    current_boss = models.ForeignKey(Boss, on_delete=models.SET_NULL, null=True)
    boss_update_time = models.DateTimeField(null=True)
