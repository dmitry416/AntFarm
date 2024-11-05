from django.shortcuts import render, redirect

from game.models import User
from other.utils import is_tg_hash_valid


def game(request):
    tg_hash = request.GET.get('hash')

    if tg_hash:
        if is_tg_hash_valid(request.GET.dict()):
            tg_id = int(request.GET['id'])
            username = request.GET.get('username')
            photo_url = request.GET.get('photo_url')

            request.session['id'] = tg_id

            user, created = User.objects.get_or_create(user_id=tg_id)
            user.image_url = photo_url if photo_url else 'https://png.pngtree.com/element_our/20200610/ourmid/pngtree-character-default-avatar-image_2237203.jpg'
            user.name = username if username else 'Hidden'

            user.save()

            return redirect('game')

    user = User.objects.get(user_id=request.session.get('id'))
    boss_img = 'images/testImage.svg'
    leaderboard = [(1, 1239123, 'User228'), (2, 123123, 'UserGandon'), (3, 123, 'Niiggaaaa'), (4, 0, 'dmitrywall.ru')]
    ants = [('images/testImage.svg', 12, 128), ('images/testImage.svg', 8, 85), ('images/testImage.svg', 3, 39)]
    total_ants = sum(map(lambda x: x[1], ants))
    items = [('images/testImage.svg', 'Капля мёда', 16), ('images/testImage.svg', 'Капля спермы', 58),
             ('images/testImage.svg', 'Залупа Артёма', 9999)]
    chest = ('images/testImage.svg', 228)

    data = {"user": user, "boss_img": boss_img, "leaderboard": leaderboard, "ants": ants, "total_ants": total_ants,
            "items": items, "chest": chest}
    return render(request, "game.html", context=data)
