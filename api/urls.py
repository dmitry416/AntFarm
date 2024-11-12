from django.urls import path

from .views import *

urlpatterns = [
    path('leaderboard/', get_leaderboard, name='leaderboard'),
    path('userants/', get_user_ants, name='userants'),
    path('useritems/', get_user_items, name='get_user_items'),
    path('usermoney/', get_user_money, name='get_user_money'),
    path('current_boss/', get_current_boss, name='current_boss'),
    path('sendall/', send_ants, name='send_ants'),
    path('getreward/', get_reward, name='get_reward'),
    path('buyant/', buy_ant, name='buy_ant'),
    path('fight_boss/', fight_boss, name='fight_boss'),
    path('sellitem/', sell_item, name='sell_item'),
    path('sellall/', sell_all_items, name='sell_all_items'),
    path('sell_chest/', sell_chest, name='sell_chest'),
    path('open_chest/', open_chest, name='open_chest'),
]
