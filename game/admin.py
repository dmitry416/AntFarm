from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Boss)
admin.site.register(ServerState)
admin.site.register(Ant)
admin.site.register(UserAnts)
admin.site.register(Chest)
admin.site.register(Item)
admin.site.register(UserItems)
admin.site.register(AntItemChance)
