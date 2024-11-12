from django.urls import path

from .views import *

urlpatterns = [
    path('leaderboard/', get_leaderboard, name='leaderboard'),
    path('userants/', get_user_ants, name='userants'),
    path('get_prices/', get_prices, name='get_prices'),
    path('current_boss/', get_current_boss, name='current_boss'),
    path('send_ants/', send_ants, name='send_ants'),
    path('buy_ant/', buy_ant, name='buy_ant'),
    path('fight_boss/', fight_boss, name='fight_boss'),
    path('sell_item/', sell_item, name='sell_item'),
    path('sell_all_items/', sell_all_items, name='sell_all_items'),
    path('sell_chest/', sell_chest, name='sell_chest'),
    path('open_chest/', open_chest, name='open_chest'),
]
