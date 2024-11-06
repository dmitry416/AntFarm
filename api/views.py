from django.http import HttpResponse, JsonResponse
from .serializers import *


def get_leaderboard(request):
    query = User.objects.order_by('-ant_count')[:20]
    data = LeaderboardSerializer(query, many=True).data
    return JsonResponse(data, safe=False)


def get_user_ants(request):
    user_id = request.session['id']
    user = User.objects.get(user_id=user_id)
    query = UserAnts.objects.filter(user=user)
    data = UserAntsSerializer(query, many=True).data
    return JsonResponse(data, safe=False)
