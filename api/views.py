from django.db.models import Sum
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .serializers import *


def get_leaderboard(request):
    query = User.objects.order_by('-ant_count')[:20]
    data = LeaderboardSerializer(query, many=True).data
    return JsonResponse(data, safe=False)


def get_user_ants(request):
    user_id = request.session['id']
    user = User.objects.get(user_id=user_id)
    query = UserAnts.objects.filter(user=user, count__gt=-1)
    data = UserAntsSerializer(query, many=True).data
    return JsonResponse(data, safe=False)


def get_user_items(request):
    user_id = request.session['id']
    user = User.objects.get(user_id=user_id)
    query = UserItems.objects.filter(user=user, count__gt=0)
    data = UserItemsSerializer(query, many=True).data
    return JsonResponse(data, safe=False)


def get_user_money(request):
    user_id = request.session['id']
    user = User.objects.get(user_id=user_id)
    return JsonResponse({'money': user.money}, safe=False)


def get_current_boss(request):
    server_state = ServerState.objects.get()
    if not server_state.current_boss:
        return JsonResponse({'error': 'no current boss found'}, status=404)

    boss_data = BossSerializer(server_state.current_boss).data
    boss_data['boss_update_time'] = server_state.boss_update_time.isoformat()
    return JsonResponse(boss_data, safe=False)


@require_POST
def send_ants(request):
    user_id = request.session.get('id')

    user = User.objects.get(user_id=user_id)
    user_ants = UserAnts.objects.filter(user=user, is_sent=False, count__gt=0)

    for user_ant in user_ants:
        return_time = timezone.now() + user_ant.ant.expedition_duration
        user_ant.is_sent = True
        user_ant.return_datetime = return_time
        user_ant.save()
    return JsonResponse({'success': True})


@require_POST
def get_reward(request):
    user_id = request.session.get('id')

    user = User.objects.get(user_id=user_id)

    current_time = timezone.now()
    user_ants = UserAnts.objects.filter(user=user, is_sent=True, return_datetime__lte=current_time)

    for user_ant in user_ants:
        user_ant.return_datetime = None
        user_ant.is_sent = False

        for _ in range(user_ant.count):
            rnd_item = user_ant.ant.get_random_item()
            user_item, _ = UserItems.objects.get_or_create(user=user, item=rnd_item)
            user_item.count += 1
            user_item.save()

        user_ant.save()

    return JsonResponse({'success': True})


@require_POST
def buy_ant(request):
    user_id = request.session.get('id')

    ant_name = request.POST.get('name')

    if not ant_name:
        return JsonResponse({'error': 'ant name is required'}, status=400)

    user = User.objects.get(user_id=user_id)
    ant = Ant.objects.get(name=ant_name)

    user_ant, _ = UserAnts.objects.get_or_create(user=user, ant=ant)
    count = user_ant.count

    if count == -1:
        return JsonResponse({'error': 'ant is blocked'}, status=400)

    if user_ant.is_sent:
        return JsonResponse({'error': 'ant is already sent'}, status=400)

    price = user_ant.get_cost()

    if user.money < price:
        return JsonResponse({'error': 'not enough money'}, status=400)

    user.money -= price
    user_ant.count += 1
    user.save()
    user_ant.save()

    return JsonResponse({'success': True, 'cost': user_ant.get_cost()}, status=200)


@require_POST
def fight_boss(request):
    user_id = request.session.get('id')

    user = User.objects.get(user_id=user_id)
    server_state = ServerState.objects.get()

    if not server_state.current_boss:
        return JsonResponse({'error': 'no current boss found'}, status=404)

    if user.chest is not None:
        return JsonResponse({'error': 'user has a chest'}, status=400)

    boss = server_state.current_boss
    available_ants = UserAnts.objects.filter(user=user, is_sent=False) \
                         .aggregate(total_count=Sum('count'))['total_count'] or 0

    if available_ants == 0:
        return JsonResponse({'error': 'no ants available for battle'}, status=400)

    win_chance = min(100, (available_ants / boss.power) * 100)

    random_number = random.randint(0, 100)
    is_victory = random_number <= win_chance

    if is_victory:
        ants_lost = min(-int(min(100 - win_chance - random_number, 0)), available_ants)
    else:
        ants_lost = min(int(max((100 - win_chance - random_number), 0) * 0.01 * available_ants), available_ants)

    if ants_lost > 0:
        ants_to_lose = list(UserAnts.objects.filter(user=user, is_sent=False).order_by('?')[:ants_lost])
        for ant_instance in ants_to_lose:
            lost_count = min(ant_instance.count, ants_lost)
            ant_instance.count -= lost_count
            ant_instance.save()
            ants_lost -= lost_count
            if ants_lost == 0:
                break

    if is_victory:
        chests = list(Chest.objects.all())
        weights = [chest.weight for chest in chests]
        selected_chest = random.choices(chests, weights=weights)[0]

        user.chest = selected_chest
        user.save()

    return JsonResponse({'success': True, 'victory': is_victory, 'ants_lost': ants_lost})


@require_POST
def sell_item(request):
    user_id = request.session.get('id')
    if not user_id:
        return JsonResponse({'error': 'user not authenticated'}, status=401)

    user = User.objects.get(user_id=user_id)
    item_name = request.POST.get('name')
    if not item_name:
        return JsonResponse({'error': 'item_name is required'}, status=400)

    item = Item.objects.get(name=item_name)
    user_item = UserItems.objects.get(user=user, item=item)

    if user_item.count <= 0:
        return JsonResponse({'error': 'you do not have this item'}, status=400)

    user.money += item.cost
    user_item.count -= 1
    user.save()
    user_item.save()
    return JsonResponse({'success': True})


@require_POST
def sell_all_items(request):
    user_id = request.session.get('id')
    user = User.objects.get(user_id=user_id)
    user_items = UserItems.objects.filter(user=user)
    total_money_earned = 0

    for user_item in user_items:
        total_money_earned += user_item.item.cost * user_item.count
        user_item.count = 0
        user_item.save()

    user.money += total_money_earned
    user.save()
    return JsonResponse({'success': True})


@require_POST
def sell_chest(request):
    user_id = request.session.get('id')

    user = User.objects.get(user_id=user_id)

    if user.chest is None:
        return JsonResponse({'error': 'no chest for sale'}, status=400)

    user.money += user.chest.cost
    user.chest = None
    user.save()
    return JsonResponse({'success': True})


@require_POST
def open_chest(request):
    user_id = request.session.get('id')
    if not user_id:
        return JsonResponse({'error': 'user not authenticated'}, status=401)

    user = User.objects.get(user_id=user_id)

    if user.chest is None:
        return JsonResponse({'error': 'no chest to open'}, status=400)

    user.chest_open = timezone.now() + timezone.timedelta(hours=2)
    user.save()
    return JsonResponse({'success': True})
