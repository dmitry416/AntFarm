from django.urls import path
from .views import *

urlpatterns = [
    path('leaderboard/', get_leaderboard, name='leaderboard'),
    path('userants/', get_user_ants, name='userants')
]
